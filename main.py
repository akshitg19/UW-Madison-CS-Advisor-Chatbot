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
# Document Loading and Processing
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Vector Stores and Embeddings
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.cross_encoders import HuggingFaceCrossEncoder

# Retrievers
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import CrossEncoderReranker

# LLMs and Chains
from langchain_community.llms import Together
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

# --- Local Imports ---
# Import the structured knowledge base from the local file.
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
    """
    Pydantic model for validating the incoming request body.
    Ensures that the 'question' field is a string.
    """
    question: str

# --- FastAPI Application Setup ---

# Initialize the FastAPI application with metadata for documentation.
app = FastAPI(
    title="UW-Madison CS Advisor API",
    description="An API for querying information about the B.S. in Computer Sciences.",
    version="1.0.0",
)

# Global variable to hold the initialized RAG chain.
# This prevents reloading the model on every request.
qa_chain = None

# --- RAG Pipeline Initialization ---

@app.on_event("startup")
def load_rag_pipeline():
    """
    This function is executed once when the FastAPI server starts.
    It loads all necessary models and sets up the full RAG pipeline.
    """
    global qa_chain
    
    # Ensure the necessary API key is available in the environment.
    if not os.getenv("TOGETHER_API_KEY"):
        raise ValueError("TOGETHER_API_KEY not found in environment.")

    # 1. Document Loading and Assembly
    # Consolidate all parts of the knowledge base into a list of LangChain Documents.
    documents = []
    cs_data_parts = [
        cs_bs_description_data, cs_bs_how_to_get_in_data, cs_bs_requirements_data, 
        cs_bs_advanced_requirements_data, cs_bs_residence_honors_data, 
        cs_bs_learning_outcomes_data, cs_bs_four_year_plan_data, cs_bs_scholarships_data,
        cs_bs_advising_careers_data
    ]
    # Combine all CS major data into one master document.
    master_cs_data = {}
    for part in cs_data_parts:
        master_cs_data.update(part)
    documents.append(Document(page_content=json.dumps(master_cs_data, indent=2), metadata={"source": "CS_BS_Major_Master_Document"}))
    
    # Create a separate document for each course.
    for course in all_course_data:
        documents.append(Document(page_content=json.dumps(course, indent=2), metadata={"source": f"{course.get('course_code', 'Unknown_Course')}.json"}))
    
    # Add documents for general university and college requirements.
    documents.append(Document(page_content=json.dumps(ls_bs_degree_requirements_data, indent=2), metadata={"source": "LS_BS_Degree_Requirements"}))
    documents.append(Document(page_content=json.dumps(university_general_education_requirements_data, indent=2), metadata={"source": "University_General_Requirements"}))

    # 2. Text Splitting
    # Break down the documents into smaller, manageable chunks for the retriever.
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    texts = text_splitter.split_documents(documents)

    # 3. Vectorization and Storage
    # Create embeddings for the text chunks and store them in a Chroma vector database.
    embedding_model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embeddings = HuggingFaceEmbeddings(model_name=embedding_model_name)
    vectorstore = Chroma.from_documents(texts, embeddings)
    
    # 4. Language Model (LLM)
    # Initialize the generative model from Together AI.
    llm = Together(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        temperature=0.1,  # Lower temperature for more factual, less creative answers.
        max_tokens=1024
    )

    # 5. Advanced Retriever Setup (Contextual Compression with Re-ranking)
    # This setup ensures the most relevant information is passed to the LLM.
    
    # a. The base retriever fetches a broad set of potentially relevant documents.
    base_retriever = vectorstore.as_retriever(search_kwargs={"k": 15})
    
    # b. The cross-encoder is a more powerful model used to re-rank the initial results.
    cross_encoder_model = HuggingFaceCrossEncoder(model_name="cross-encoder/ms-marco-MiniLM-L-6-v2")
    compressor = CrossEncoderReranker(model=cross_encoder_model, top_n=4)
    
    # c. The final retriever compresses the results, passing only the top N documents.
    compression_retriever = ContextualCompressionRetriever(
        base_compressor=compressor, base_retriever=base_retriever
    )

    # 6. Prompt Engineering
    # Define the instructions for the LLM to guide its response generation.
    template = """
You are a formal, expert academic advisor for the University of Wisconsin-Madison's Computer Sciences department.
Your tone should be professional, helpful, and precise.
Use the following highly relevant context to provide a direct and accurate answer to the user's question.
Do not repeat the question or use a question-and-answer format.
If you are listing multiple items, such as courses, use a Markdown bulleted list.
If the answer is not in the provided context, state that you cannot find the information based on the documents available.

Context:
{context}

Question: {question}
Answer:"""
    prompt = PromptTemplate(template=template, input_variables=["context", "question"])

    # 7. Chain Assembly
    # Combine the retriever, prompt, and LLM into a single, runnable chain.
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
    """
    The main endpoint for handling user queries.
    It takes a question, invokes the RAG chain, and returns the answer.
    """
    if not qa_chain:
        # This case should ideally not be hit if the startup event is successful.
        raise HTTPException(status_code=503, detail="RAG pipeline is not ready.")
    try:
        # Invoke the RAG chain with the user's question.
        result = qa_chain.invoke({"query": query.question})
        return {"answer": result['result']}
    except Exception as e:
        # Generic error handling for any issues during the RAG chain execution.
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    """
    A simple health check endpoint to confirm that the API is running.
    """
    return {"status": "UW-Madison CS Advisor API is running."}
