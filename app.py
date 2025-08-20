"""
Streamlit Frontend for the UW-Madison CS Advisor Chatbot.

This script creates the user-facing web interface for the RAG-powered chatbot.
It's been updated to handle conversational sessions, providing a more natural
and context-aware user experience.

Author: Akshit Ganesh
Date: 8/3/25
"""

import streamlit as st
import requests
import sys

# --- Application Configuration ---

def get_backend_url():
    """
    Retrieves the backend API URL from command-line arguments.
    This allows for flexible deployment.
    """
    if len(sys.argv) > 2 and sys.argv[1] == '--fastapiUrl':
        return sys.argv[2]
    else:
        # Default for local development.
        return "http://127.0.0.1:8000/query"

FASTAPI_URL = get_backend_url()

# --- UI Layout and Content ---

def setup_sidebar():
    """
    Configures the Streamlit sidebar with app information and tech stack details.
    """
    with st.sidebar:
        st.title("UW-Madison CS Advisor 🤖")
        st.markdown(
            "This chatbot provides expert information on the B.S. in Computer "
            "Sciences at the University of Wisconsin-Madison."
        )
        st.markdown(
            "Ask a question to get a fast response from our AI-powered advisor!"
        )
        st.info(f"Connected to Backend: `{FASTAPI_URL.replace('/query', '')}`")

        with st.expander("⚙️ Technologies Used", expanded=False):
            st.markdown("""
            **Core Concept:** Conversational Retrieval-Augmented Generation (RAG)
            
            **Backend:**
            - **Framework:** FastAPI
            - **AI/ML Orchestration:** LangChain
            - **LLM Provider:** Together AI (`Mistral-7B-Instruct-v0.2`)
            - **Vector Database:** ChromaDB
            - **Embeddings Model:** `all-MiniLM-L6-v2`
            - **Re-ranking Model:** `ms-marco-MiniLM-L-6-v2`
            - **Chat History:** SQLite
            
            **Frontend:**
            - **Framework:** Streamlit
            """)

# --- Chat Logic and State Management ---

def initialize_session_state():
    """
    Initializes session state variables if they don't exist. This is crucial
    for maintaining the conversation across reruns.
    """
    # This holds the list of messages for displaying the chat history.
    if "messages" not in st.session_state:
        st.session_state.messages = [{
            "role": "assistant",
            "content": "Hello! How can I help you with the Computer Sciences major today?"
        }]
    # This holds the unique session ID for the current conversation.
    if "session_id" not in st.session_state:
        st.session_state.session_id = None

def display_chat_messages():
    """
    Renders the chat history from session state to the UI.
    """
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def handle_user_input():
    """
    Manages user input, communication with the backend, and updates the chat display.
    This is the core interactive loop of the application.
    """
    if prompt := st.chat_input("Ask a question about the CS major..."):
        # 1. Add user's message to the UI and history.
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # 2. Prepare for and display the assistant's response.
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            with st.spinner("Connecting to the advisor..."):
                try:
                    # 3. Send the request to the backend.
                    # This now includes the session_id to maintain conversation context.
                    payload = {
                        "question": prompt,
                        "session_id": st.session_state.session_id
                    }
                    response = requests.post(FASTAPI_URL, json=payload, timeout=120)
                    response.raise_for_status()
                    
                    result = response.json()
                    answer = result.get("answer", "I apologize, but I couldn't retrieve an answer.")
                    
                    # 4. CRITICAL: Update the session ID with the one from the backend.
                    # The backend generates a new ID for the first message of a conversation.
                    st.session_state.session_id = result.get("session_id")

                    # 5. Display the answer and add it to the chat history.
                    message_placeholder.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})

                except requests.exceptions.RequestException as e:
                    error_message = (
                        "**Error:** Could not connect to the advisor API. "
                        "Please ensure the backend server is running and the URL is correct.\n\n"
                        f"`{str(e)}`"
                    )
                    message_placeholder.error(error_message)
                    st.session_state.messages.append({"role": "assistant", "content": error_message})
                except Exception as e:
                    error_message = f"**An unexpected error occurred:**\n\n`{str(e)}`"
                    message_placeholder.error(error_message)
                    st.session_state.messages.append({"role": "assistant", "content": error_message})

# --- Main Application Execution ---

def main():
    """
    Main function to run the Streamlit application.
    """
    st.set_page_config(page_title="UW-Madison CS Advisor", layout="centered")
    
    setup_sidebar()
    st.header("Chat with the CS Advisor")
    
    initialize_session_state()
    display_chat_messages()
    handle_user_input()

if __name__ == "__main__":
    main()
