"""
Streamlit Frontend for the UW-Madison CS Advisor Chatbot.

This script creates the user-facing web interface for the RAG-powered chatbot.
It is designed to be lightweight and fast, offloading all heavy AI/ML processing
to a separate FastAPI backend.

Author: Akshit Ganesh
Date: 8/3/25
"""

import streamlit as st
import requests
import os
import sys

# --- Application Configuration ---

def get_backend_url():
    """
    Retrieves the backend API URL from command-line arguments.
    This allows for flexible deployment by passing the backend endpoint
    when starting the Streamlit app.
    
    Returns:
        str: The fully-formed URL for the backend query endpoint.
    """
    # Check if the custom command-line argument '--fastapiUrl' is provided
    if len(sys.argv) > 2 and sys.argv[1] == '--fastapiUrl':
        # The URL is the argument that follows '--fastapiUrl'
        return sys.argv[2]
    else:
        # Fallback to a default local URL if no argument is provided.
        # This is useful for local development outside of the Colab environment.
        return "[http://127.0.0.1:8000/query](http://127.0.0.1:8000/query)"

FASTAPI_URL = get_backend_url()

# --- UI Layout and Content ---

def setup_sidebar():
    """
    Configures and populates the Streamlit sidebar.
    This includes the app title, description, and a section detailing the
    technologies used, which is valuable for portfolio presentation.
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
        # Display the connected backend URL for debugging and transparency.
        st.info(f"Connected to Backend: `{FASTAPI_URL.replace('/query', '')}`")

        # An expandable section for recruiters and curious users to see the tech stack.
        with st.expander("⚙️ Technologies Used", expanded=False):
            st.markdown("""
            **Core Concept:** Retrieval-Augmented Generation (RAG)
            
            **Backend:**
            - **Framework:** FastAPI
            - **AI/ML Orchestration:** LangChain
            - **LLM Provider:** Together AI (`Mistral-7B-Instruct-v0.2`)
            - **Vector Database:** ChromaDB
            - **Embeddings Model:** `all-MiniLM-L6-v2`
            - **Re-ranking Model:** `ms-marco-MiniLM-L-6-v2`
            
            **Frontend:**
            - **Framework:** Streamlit
            
            **Deployment & Tunneling:**
            - Google Colab
            - Ngrok (Backend)
            - Localtunnel (Frontend)
            """)

def initialize_chat_history():
    """
    Sets up the chat history in Streamlit's session state if it doesn't exist.
    This ensures that the conversation is preserved across user interactions
    and app reruns.
    """
    if "messages" not in st.session_state:
        st.session_state.messages = [{
            "role": "assistant",
            "content": "Hello! How can I help you with the Computer Sciences major today?"
        }]

def display_chat_messages():
    """
    Renders the chat history to the UI.
    It iterates through the messages stored in the session state and displays
    them using the appropriate chat message format.
    """
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def handle_user_input():
    """
    Manages the user input, backend communication, and response display.
    This is the main interactive loop of the chatbot.
    """
    # `st.chat_input` creates a text input field fixed to the bottom of the page.
    if prompt := st.chat_input("Ask a question about the CS major..."):
        # 1. Add the user's message to the chat history and display it.
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # 2. Process and display the assistant's response.
        with st.chat_message("assistant"):
            # Use a placeholder for a smoother "streaming" feel.
            message_placeholder = st.empty()
            with st.spinner("Thinking..."):
                try:
                    # 3. Send the user's prompt to the FastAPI backend.
                    payload = {"question": prompt}
                    response = requests.post(FASTAPI_URL, json=payload, timeout=120)
                    # Raise an error for bad status codes (e.g., 404, 500).
                    response.raise_for_status()
                    
                    # 4. Extract the answer from the JSON response.
                    result = response.json()
                    answer = result.get("answer", "I apologize, but I couldn't retrieve an answer.")
                    
                    # 5. Display the answer and add it to the chat history.
                    message_placeholder.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})

                # Handle specific network errors for clearer user feedback.
                except requests.exceptions.RequestException as e:
                    error_message = (
                        "**Error:** Could not connect to the advisor API. "
                        "Please ensure the backend server is running and the URL is correct.\n\n"
                        f"`{str(e)}`"
                    )
                    message_placeholder.error(error_message)
                    st.session_state.messages.append({"role": "assistant", "content": error_message})
                # Handle all other potential errors.
                except Exception as e:
                    error_message = f"**An unexpected error occurred:**\n\n`{str(e)}`"
                    message_placeholder.error(error_message)
                    st.session_state.messages.append({"role": "assistant", "content": error_message})

# --- Main Application Execution ---

def main():
    """
    Main function to run the Streamlit application.
    """
    st.set_page_config(page_title="UW-Madison CS Advisor", layout="wide")
    
    setup_sidebar()
    st.header("Chat with the CS Advisor")
    
    initialize_chat_history()
    display_chat_messages()
    handle_user_input()

if __name__ == "__main__":
    main()