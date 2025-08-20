"""
Backend API for the UW-Madison CS Advisor Chatbot.

This script sets up a FastAPI server that hosts the core Retrieval-Augmented
Generation (RAG) pipeline. It handles document processing, embedding, retrieval,
and generation, exposing a simple endpoint for the frontend to query.

Author: Akshit Ganesh
Date: 8/3/25
"""

# --- Core Imports ---
import json
import os
import uuid
from typing import Optional
import uvicorn

# --- FastAPI Imports ---
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# --- LangChain Imports ---
# I've added a bunch of new imports here to support conversational chains.
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
from dotenv import load_dotenv

load_dotenv()

# --- Local Imports ---
# Importing my knowledge base and the new database utility functions.
from knowledge_base import (
    cs_bs_description_data, cs_bs_how_to_get_in_data, cs_bs_requirements_data,
    cs_bs_advanced_requirements_data, cs_bs_residence_honors_data,
    cs_bs_learning_outcomes_data, cs_bs_four_year_plan_data,
    cs_bs_scholarships_data, cs_bs_advising_careers_data,
    all_course_data, ls_bs_degree_requirements_data,
    university_general_education_requirements_data
)
from database_utils import get_chat_history, add_message_to_history

# --- Data Models ---

class Query(BaseModel):
    """
    Updated the Pydantic model. Now it expects a question and
    an optional session_id for tracking conversations.
    """
    question: str
    session_id: Optional[str] = None

# --- FastAPI Application Setup ---

# The main FastAPI app instance. The metadata helps with auto-generated docs.
app = FastAPI(
    title="UW-Madison CS Advisor API",
    description="An API for querying information about the B.S. in Computer Sciences.",
    version="1.0.0",
)

# I'm changing the global variable to only hold the retriever.
# The retriever (with its vector store) is static and can be loaded once.
# The full chain, however, needs to be built on each request to include the chat history.
compression_retriever = None

# --- RAG Pipeline Initialization ---

@app.on_event("startup")
def load_retriever():
    """
    This function now only loads the components that don't change between requests:
    the documents, the vector store, and the final retriever.
    This runs once when the server starts up.
    """
    global compression_retriever
    
    # Quick check to make sure the API key is actually set.
    if not os.getenv("TOGETHER_API_KEY"):
        raise ValueError("TOGETHER_API_KEY not found in environment.")

    # Step 1: Loading my data into LangChain's Document format.
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

    # Step 2: Splitting the documents into smaller chunks for the vector store.
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    texts = text_splitter.split_documents(documents)

    # Step 3: Turning the text chunks into vectors and storing them in ChromaDB.
    embedding_model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embeddings = HuggingFaceEmbeddings(model_name=embedding_model_name)
    vectorstore = Chroma.from_documents(texts, embeddings)
    
    # Step 4: Building the final retriever with re-ranking.
    base_retriever = vectorstore.as_retriever(search_kwargs={"k": 12})
    cross_encoder_model = HuggingFaceCrossEncoder(model_name="cross-encoder/ms-marco-MiniLM-L-6-v2")
    compressor = CrossEncoderReranker(model=cross_encoder_model, top_n=4)
    
    # This retriever is now stored globally, ready to be used by any request.
    compression_retriever = ContextualCompressionRetriever(
        base_compressor=compressor, base_retriever=base_retriever
    )
    print("Retriever loaded successfully.")

# --- Conversational Chain Creation ---

def create_conversational_rag_chain(retriever):
    """
    This function builds the full conversational RAG chain. It's designed to be
    called on each request so it can incorporate the specific chat history.
    """
    # I'm using a new LLM instance here just to keep this function self-contained.
    llm = Together(model="mistralai/Mistral-7B-Instruct-v0.2", temperature=0.2, max_tokens=1024)

    # 1. Contextualizing Prompt: This is the first new piece. Its job is to take the
    # chat history and the new question, and rephrase it into a standalone question.
    # This is key for making the retriever work with follow-up questions.
    contextualize_q_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "Given a chat history and the latest user question which might reference context in the chat history, formulate a standalone question which can be understood without the chat history. Do NOT answer the question, just reformulate it if needed and otherwise return it as is."),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )
    
    # 2. History-Aware Retriever: This is a special LangChain component that wraps my
    # base retriever. It uses the LLM and the prompt above to do the question rephrasing
    # before actually fetching any documents.
    history_aware_retriever = create_history_aware_retriever(
        llm, retriever, contextualize_q_prompt
    )

    # 3. Final QA Prompt: This prompt is for the final answer generation. It gets
    # the rephrased question, the retrieved documents (context), and the chat history.
    qa_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a friendly and knowledgeable academic advisor for the University of Wisconsin-Madison's Computer Sciences department. Use the following retrieved context to answer the user's question. If the question is direct and simple, provide a direct and concise answer. Be comprehensive when asked for lists.\n\nContext:\n{context}"),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )

    # 4. Document Combination Chain: This is a simple chain that just takes the
    # retrieved documents and "stuffs" them into the final QA prompt.
    question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)
    
    # 5. Final Retrieval Chain: This is the final chain that ties everything together.
    # It runs the history-aware retriever first, then passes the results to the QA chain.
    rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)
    
    return rag_chain

# --- API Endpoints ---

@app.post("/query")
def get_answer(query: Query):
    """
    This is the main endpoint. It now manages sessions and builds the
    conversational chain for each request.
    """
    if not compression_retriever:
        # Fallback in case the retriever didn't load on startup.
        raise HTTPException(status_code=503, detail="Retriever is not ready.")

    # 1. Session Management: If the frontend doesn't send a session_id,
    # I'll create a new one. This marks the start of a new conversation.
    session_id = query.session_id if query.session_id else str(uuid.uuid4())

    # 2. History Retrieval: I'll fetch the past messages for this specific session
    # from our SQLite database. For a new session, this will be an empty list.
    chat_history = get_chat_history(session_id)

    # 3. Dynamic Chain Creation: I build the full RAG chain here, inside the request.
    # This ensures it has the most up-to-date chat history for context.
    conversational_rag_chain = create_conversational_rag_chain(compression_retriever)

    try:
        # 4. Invoking the Chain: I pass the user's question and the chat history.
        # The chain handles the rest: rephrasing, retrieving, and answering.
        result = conversational_rag_chain.invoke(
            {"input": query.question, "chat_history": chat_history}
        )
        answer = result.get("answer", "I apologize, but I couldn't retrieve an answer.")

        # 5. Storing the new messages: After getting an answer, I save both the
        # user's question and the AI's response to the database for the next turn.
        add_message_to_history(session_id, 'human', query.question)
        add_message_to_history(session_id, 'ai', answer)

        # 6. Sending the Response: I send back the answer and the session_id.
        # The frontend needs to store this ID and send it back with the next question.
        return {"answer": answer, "session_id": session_id}
        
    except Exception as e:
        # A general error handler if anything goes wrong.
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    """A simple health check endpoint so I can see if the API is running."""
    return {"status": "UW-Madison CS Advisor API is running."}

