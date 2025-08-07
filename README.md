# UW-Madison CS Advisor Chatbot

This is an advanced, AI-powered chatbot designed to answer questions about the B.S. in Computer Sciences at the University of Wisconsin-Madison. It uses a Retrieval-Augmented Generation (RAG) architecture to provide accurate, context-aware answers based on the official university course guide.

This project demonstrates a scalable, decoupled system with a dedicated backend for AI processing and a lightweight, responsive frontend for user interaction.

---
## 🎥 Demo

[![UW-Madison CS Advisor Chatbot Demo](https://i.imgur.com/RpzW1iD.png)](https://mediaspace.wisc.edu/media/Recording+2/1_d7l5msp4)

*Click the thumbnail above to watch a video demo of the application.*

---

## 🚀 Features

-   **Conversational Q&A:** Ask questions in natural language.
-   **High Accuracy:** Utilizes a re-ranking retriever to find the most relevant information and reduce model hallucinations.
-   **Fast & Responsive UI:** The Streamlit frontend is decoupled from the heavy AI models, ensuring a smooth user experience.
-   **Scalable Architecture:** The FastAPI backend can be scaled independently to handle heavy computational loads.

---

## 🏛️ Architecture Overview

The application is split into two main components:

1.  **FastAPI Backend (`main.py`):** A robust API that handles the entire RAG pipeline. It loads the knowledge base, manages the vector store, and runs the language model to generate answers. All heavy lifting is done here.
2.  **Streamlit Frontend (`app.py`):** A lightweight web application that provides the user interface. It does not load any models. When a user asks a question, it simply makes an API call to the backend and displays the response.

## 🛠️ Tech Stack

-   **Core Concept:** Retrieval-Augmented Generation (RAG)
-   **Backend:**
    -   **Framework:** FastAPI
    -   **AI/ML Orchestration:** LangChain
    -   **LLM Provider:** Together AI (`Mistral-7B-Instruct-v0.2`)
    -   **Vector Database:** ChromaDB
    -   **Embeddings Model:** `sentence-transformers/all-MiniLM-L6-v2`
    -   **Re-ranking Model:** `cross-encoder/ms-marco-MiniLM-L-6-v2`
-   **Frontend:**
    -   **Framework:** Streamlit
-   **Language:** Python 3.11+

---

## ⚙️ Local Setup and Installation

Follow these steps to run the project on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/akshitg19/UW-Madison-CS-Advisor-Chatbot.git
cd UW-Madison-CS-Advisor-Chatbot
```

### 2. Set Up a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

```bash
# Create a virtual environment
python -m venv venv

# Activate it (on macOS/Linux)
source venv/bin/activate

# Or on Windows
# venv\Scripts\activate
```

### 3. Install Dependencies

Install all required packages from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

You need an API key from [Together.ai](https://www.together.ai/) to run the language model.

1.  Create a file named `.env` in the root of your project directory.
2.  Add your API key to this file:

    ```
    TOGETHER_API_KEY="your_api_key_here"
    ```

The `main.py` script is configured to automatically load this key.

### 5. Run the Application

You need to run the backend and frontend servers in two separate terminal windows.

**In your first terminal, start the backend server:**

```bash
# This will start the FastAPI server.
# Wait for it to display "RAG Pipeline loaded successfully..."
uvicorn main:app --host 0.0.0.0 --port 8000
```

**In your second terminal, start the Streamlit frontend:**

```bash
# This will start the Streamlit app and open it in your browser.
streamlit run app.py
```

You should now be able to interact with your chatbot at `http://localhost:8501`.

---

## 📁 Project Structure

```
.
├── app.py              # The Streamlit frontend application
├── main.py             # The FastAPI backend and RAG pipeline
├── knowledge_base.py   # The raw data for the knowledge base
├── requirements.txt    # Project dependencies
└── README.md           # This file
```
