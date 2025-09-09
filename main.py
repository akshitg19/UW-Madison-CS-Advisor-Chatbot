"""
Provides the serverless backend for the UW-Madison CS Advisor chatbot.

This service uses FastAPI and is designed for deployment on AWS Lambda. It exposes
an API endpoint that leverages a Retrieval-Augmented Generation (RAG) pipeline
built with LangChain to answer user queries. Conversation history is maintained
using Amazon DynamoDB.

Author: Akshit Ganesh
Date: 9/8/25
"""

# --- Core Imports ---
import json
import os
import uuid
from typing import Optional

# --- AWS & Serverless Imports ---
import boto3
from mangum import Mangum # Adapter for running FastAPI on AWS Lambda

# --- FastAPI Imports ---
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# --- LangChain Imports ---
# Components for building the conversational RAG pipeline.
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.cross_encoders import HuggingFaceCrossEncoder
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import CrossEncoderReranker
from langchain_community.llms import Together
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

# --- Local Imports ---
# Knowledge base content, packaged with the deployment.
from knowledge_base import (
    cs_bs_description_data, cs_bs_how_to_get_in_data, cs_bs_requirements_data,
    cs_bs_advanced_requirements_data, cs_bs_residence_honors_data,
    cs_bs_learning_outcomes_data, cs_bs_four_year_plan_data,
    cs_bs_scholarships_data, cs_bs_advising_careers_data,
    all_course_data, ls_bs_degree_requirements_data,
    university_general_education_requirements_data
)

# --- AWS Setup ---
# Initialize the DynamoDB client.
# In the AWS Lambda environment, authentication is handled automatically by the execution role.
dynamodb = boto3.resource('dynamodb')
chat_history_table = dynamodb.Table('ChatbotHistory')

# --- Data Models ---
class ChatRequest(BaseModel):
    """Defines the expected structure for incoming API requests."""
    question: str
    session_id: Optional[str] = None

# --- FastAPI Application Setup ---
app = FastAPI(
    title="UW-Madison CS Advisor API (AWS)",
    description="An API for querying information about the B.S. in Computer Sciences, adapted for AWS Lambda.",
    version="1.1.0",
)

# The retriever model is defined globally. This is a performance optimization for
# AWS Lambda, allowing the model to be loaded only once during a "cold start"
# and reused across subsequent "warm" invocations.
compression_retriever = None

# --- RAG Pipeline Initialization ---

@app.on_event("startup")
def load_retriever():
    """
    This startup event handler initializes the core RAG retriever model. This
    process runs only once when the service starts, ensuring the model is
    ready to handle requests efficiently.
    """
    global compression_retriever
    
    # Verify that the necessary API key is configured.
    if not os.getenv("TOGETHER_API_KEY"):
        raise ValueError("TOGETHER_API_KEY not found in environment.")

    # 1. Load and structure knowledge base content from various sources.
    documents = []
    cs_data_parts = [
        cs_bs_description_data, cs_bs_how_to_get_in_data, cs_bs_requirements_data, 
        cs_bs_advanced_requirements_data, cs_bs_residence_honors_data, 
        cs_bs_learning_outcomes_data, cs_bs_four_year_plan_data, cs_bs_scholarships_data,
        cs_bs_advising_careers_data
    ]
    master_cs_data = {}
    for part in cs_data_parts:
        master_cs_data.update(part)
    documents.append(Document(page_content=json.dumps(master_cs_data, indent=2), metadata={"source": "CS_BS_Major_Master_Document"}))
    
    for course in all_course_data:
        documents.append(Document(page_content=json.dumps(course, indent=2), metadata={"source": f"{course.get('course_code', 'Unknown_Course')}.json"}))
    
    documents.append(Document(page_content=json.dumps(ls_bs_degree_requirements_data, indent=2), metadata={"source": "LS_BS_Degree_Requirements"}))
    documents.append(Document(page_content=json.dumps(university_general_education_requirements_data, indent=2), metadata={"source": "University_General_Requirements"}))

    # 2. Segment the documents into smaller, more manageable chunks for efficient processing.
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    texts = text_splitter.split_documents(documents)

    # 3. Convert text chunks into numerical vectors (embeddings) and load them into an in-memory vector store.
    embedding_model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embeddings = HuggingFaceEmbeddings(model_name=embedding_model_name)
    vectorstore = Chroma.from_documents(texts, embeddings)
    
    # 4. Configure the final retriever, which combines the vector store with a re-ranking model to improve search relevance.
    base_retriever = vectorstore.as_retriever(search_kwargs={"k": 12})
    cross_encoder_model = HuggingFaceCrossEncoder(model_name="cross-encoder/ms-marco-MiniLM-L-6-v2")
    compressor = CrossEncoderReranker(model=cross_encoder_model, top_n=4)
    
    # The fully configured retriever is stored in the global scope for reuse.
    compression_retriever = ContextualCompressionRetriever(
        base_compressor=compressor, base_retriever=base_retriever
    )
    print("Retriever loaded successfully.")

# --- DynamoDB Helper Functions ---

def get_chat_history_from_dynamo(session_id: str):
    """
    Retrieves and formats the chat history for a given session from DynamoDB.
    """
    history = []
    try:
        response = chat_history_table.get_item(Key={'session_id': session_id})
        if 'Item' in response and 'messages' in response['Item']:
            messages = response['Item']['messages']
            for msg in messages:
                if msg['type'] == 'human':
                    history.append(HumanMessage(content=msg['content']))
                elif msg['type'] == 'ai':
                    history.append(AIMessage(content=msg['content']))
    except Exception as e:
        print(f"Error getting history from DynamoDB: {e}")
    return history

def save_messages_to_dynamo(session_id: str, human_message: str, ai_message: str):
    """
    Saves the latest user query and AI response to the session's chat history in DynamoDB.
    """
    try:
        # Appends new messages to the list, or creates the list if it doesn't exist.
        chat_history_table.update_item(
            Key={'session_id': session_id},
            UpdateExpression="SET messages = list_append(if_not_exists(messages, :empty_list), :new_messages)",
            ExpressionAttributeValues={
                ':new_messages': [
                    {'type': 'human', 'content': human_message},
                    {'type': 'ai', 'content': ai_message}
                ],
                ':empty_list': []
            }
        )
    except Exception as e:
        print(f"Error saving messages to DynamoDB: {e}")

# --- Conversational Chain Creation ---

def create_conversational_rag_chain(retriever):
    """
    Constructs the complete conversational RAG chain on a per-request basis.
    This dynamic creation allows the inclusion of a specific user's chat
    history for contextual understanding.
    """
    llm = Together(model="mistralai/Mistral-7B-Instruct-v0.2", temperature=0.2, max_tokens=1024)

    # 1. Define a prompt to rephrase the user's latest question into a standalone
    #    query, using the conversation history for context.
    contextualize_q_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "Given a chat history and the latest user question which might reference context in the chat history, formulate a standalone question which can be understood without the chat history. Do NOT answer the question, just reformulate it if needed and otherwise return it as is."),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )
    
    # 2. Create a history-aware retriever that uses the above prompt to reformulate
    #    the question before searching the knowledge base.
    history_aware_retriever = create_history_aware_retriever(
        llm, retriever, contextualize_q_prompt
    )

    # 3. Define the main prompt for the AI, instructing it on its persona ('BadgerBot'),
    #    rules for answering, and how to use the retrieved context.
    qa_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", """
    You are 'BadgerBot', the official AI academic advisor for the UW-Madison Computer Sciences department. Your persona is helpful, encouraging, and highly professional. Your sole purpose is to provide accurate information to students based on the official documents provided.
    
    **Core Task:**
    Analyze the user's `input` and the `chat_history` to understand their question fully. Then, carefully search the `context` to construct a comprehensive and accurate answer.
    
    **Rules of Engagement:**
    1.  **Strictly Grounded:** Base your entire answer *only* on the information found in the `context`. Do not use any external knowledge or make assumptions.
    2.  **Acknowledge Missing Information:** If the answer is not found in the `context`, you MUST state: "I'm sorry, but I couldn't find specific information about that in the provided documents."
    3.  **Synthesize, Don't Just Recite:** If multiple pieces of the context are relevant, synthesize them into a single, coherent answer.
    4.  **Formatting:** Use Markdown for clarity.
        - Use bullet points (`-`) for lists (e.g., course requirements, career resources).
        - Use bold text (`**text**`) for key terms like course codes, GPAs, or important deadlines.
    5.  **Role-Play:** You are the 'assistant'. After providing your answer, you must stop. Do not generate a 'human' response or ask a follow-up question.
    
    Context:
    {context}
    """),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )

    # 4. Create a chain to feed the retrieved documents into the main QA prompt.
    question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)
    
    # 5. Assemble the final chain, orchestrating the history-aware retrieval and the final answer generation steps.
    rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)
    
    return rag_chain

# --- API Endpoints ---
@app.post("/chat")
def get_answer(request: ChatRequest):
    """
    Main API endpoint to process user queries. It orchestrates session
    management, history retrieval, RAG chain execution, and response storage.
    """
    if not compression_retriever:
        raise HTTPException(status_code=503, detail="Retriever is not ready.")

    # 1. Manage the conversation session. If no session_id is provided, a new one is created.
    session_id = request.session_id if request.session_id else str(uuid.uuid4())

    # 2. Fetch the conversation history for the current session from DynamoDB.
    chat_history = get_chat_history_from_dynamo(session_id)

    # 3. Dynamically construct the conversational RAG chain, injecting the retrieved chat history.
    conversational_rag_chain = create_conversational_rag_chain(compression_retriever)

    try:
        # 4. Execute the RAG chain with the user's question to generate an answer.
        result = conversational_rag_chain.invoke(
            {"input": request.question, "chat_history": chat_history}
        )
        answer = result.get("answer", "I apologize, but I couldn't retrieve an answer.")

        # 5. Persist the new question and the AI's answer to the session history in DynamoDB.
        save_messages_to_dynamo(session_id, request.question, answer)

        # 6. Return the generated answer and the session_id to the client.
        return {"answer": answer, "session_id": session_id}
        
    except Exception as e:
        # General error handler for the RAG chain process.
        print(f"Error during chain invocation: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while processing your request.")

@app.get("/")
def read_root():
    """Provides a simple health check endpoint to confirm the service is operational."""
    return {"status": "UW-Madison CS Advisor API is running."}

# The Mangum handler acts as an adapter, allowing the FastAPI application to
# run within the AWS Lambda environment.
handler = Mangum(app)

