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
import logging
import uvicorn

# --- FastAPI Imports ---
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# --- LangChain Imports ---
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.cross_encoders import HuggingFaceCrossEncoder
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import CrossEncoderReranker
from langchain_community.llms import Together
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

# --- Local Imports ---
from knowledge_base import (
    cs_bs_description_data, cs_bs_how_to_get_in_data, cs_bs_requirements_data,
    cs_bs_advanced_requirements_data, cs_bs_residence_honors_data,
    cs_bs_learning_outcomes_data, cs_bs_four_year_plan_data,
    cs_bs_scholarships_data, cs_bs_advising_careers_data,
    all_course_data, ls_bs_degree_requirements_data,
    university_general_education_requirements_data
)

# --- Data Models ---

class Query(BaseModel):
    """Simple Pydantic model to make sure the question is a string."""
    question: str

# --- FastAPI Application Setup ---

# The main FastAPI app instance. The metadata helps with auto-generated docs.
app = FastAPI(
    title="UW-Madison CS Advisor API",
    description="An API for querying information about the B.S. in Computer Sciences.",
    version="1.0.0",
)

# I'm using a global variable for the chain so it's loaded only once on startup.
# This prevents reloading the heavy models on every single API request.
qa_chain = None

# --- RAG Pipeline Initialization ---

@app.on_event("startup")
def load_rag_pipeline():
    """
    This function gets triggered once when the server starts.
    It builds the entire RAG pipeline from scratch and stores it in our global variable.
    """
    global qa_chain
    
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
    # I decided to combine all the general CS major info into one big document.
    # This helps the retriever find broad context for complex questions.
    master_cs_data = {}
    for part in cs_data_parts:
        master_cs_data.update(part)
    documents.append(Document(page_content=json.dumps(master_cs_data, indent=2), metadata={"source": "CS_BS_Major_Master_Document"}))
    
    # For courses, I'm creating a separate document for each one. This way,
    # questions about a specific course can be answered more accurately.
    for course in all_course_data:
        documents.append(Document(page_content=json.dumps(course, indent=2), metadata={"source": f"{course.get('course_code', 'Unknown_Course')}.json"}))
    
    # Adding the last couple of general requirement documents.
    documents.append(Document(page_content=json.dumps(ls_bs_degree_requirements_data, indent=2), metadata={"source": "LS_BS_Degree_Requirements"}))
    documents.append(Document(page_content=json.dumps(university_general_education_requirements_data, indent=2), metadata={"source": "University_General_Requirements"}))

    # Step 2: Splitting the documents into smaller chunks for the vector store.
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    texts = text_splitter.split_documents(documents)

    # Step 3: Turning the text chunks into vectors and storing them in ChromaDB.
    embedding_model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embeddings = HuggingFaceEmbeddings(model_name=embedding_model_name)
    vectorstore = Chroma.from_documents(texts, embeddings)
    
    # Step 4: Setting up the LLM I'll be using for the "generation" part.
    llm = Together(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        temperature=0.2,
        max_tokens=1024
    )

    # Step 5: Building a better retriever. A simple vector search isn't always enough.
    # The first pass gets a broad set of 12 potentially relevant documents.
    base_retriever = vectorstore.as_retriever(search_kwargs={"k": 12})
    
    # This cross-encoder then re-ranks those 12 documents to find the best 4.
    # It's a slower but much more accurate way to find the right context.
    cross_encoder_model = HuggingFaceCrossEncoder(model_name="cross-encoder/ms-marco-MiniLM-L-6-v2")
    compressor = CrossEncoderReranker(model=cross_encoder_model, top_n=4)
    
    # This wraps it all together into a single retriever.
    compression_retriever = ContextualCompressionRetriever(
        base_compressor=compressor, base_retriever=base_retriever
    )

    # Step 6: Crafting the prompt. This is how I tell the LLM how to behave.
    template = """
    You are a friendly and knowledgeable academic advisor for the University of Wisconsin-Madison's Computer Sciences department. Your goal is to provide clear, helpful, and encouraging guidance to students.

    Carefully read the user's question and the provided context.
    - First, acknowledge the user's specific situation if they provide one (e.g., "It's great that you already have credit for...").
    - Then, use the context to directly answer their question in a human-like, conversational manner.
    - **If the question is direct and simple (e.g., asking for credits, prerequisites), provide a direct and concise answer.**
    - For more complex or open-ended questions, answer in a more detailed, conversational manner.
    - **IMPORTANT**: When the user asks for a list of items (like courses), ensure your answer is comprehensive and includes all relevant items found in the context.
    - Use a Markdown bulleted list for clarity when listing items.
    - If the answer is not in the provided context, state that you cannot find the specific information based on the documents available.

    Context:
    {context}

    Question: {question}
    Answer:"""
    prompt = PromptTemplate(template=template, input_variables=["context", "question"])

    # Step 7: Assembling the final chain that connects the retriever, prompt, and LLM.
    qa_chain = RetrievalQA.from_chain_type(
        llm,
        chain_type="stuff",
        retriever=compression_retriever,
        chain_type_kwargs={"prompt": prompt}
    )
    print("RAG Pipeline loaded successfully using Re-ranking Retriever.")

# --- API Endpoints ---

@app.post("/query")
def get_answer(query: Query):
    """This is the main endpoint the frontend will call."""
    if not qa_chain:
        # This is a fallback just in case the server starts but the chain fails to load.
        raise HTTPException(status_code=503, detail="RAG pipeline is not ready.")
    try:
        # Here's where the magic happens: run the query through the RAG chain.
        result = qa_chain.invoke({"query": query.question})
        return {"answer": result['result']}
    except Exception as e:
        # A general error handler if anything goes wrong during the chain execution.
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    """A simple health check endpoint so I can see if the API is running."""
    return {"status": "UW-Madison CS Advisor API is running."}
