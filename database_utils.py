
import sqlite3
from langchain.schema import HumanMessage, AIMessage

# --- Database Setup ---

def get_db_connection():
    """Establishes a connection to the SQLite database."""
    conn = sqlite3.connect('rag_app.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_chat_history_table():
    """Creates the chat_history table if it doesn't already exist."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT NOT NULL,
            message_type TEXT NOT NULL,
            content TEXT NOT NULL
        );
    """)
    conn.commit()
    conn.close()
    print("Database and chat_history table are ready.")

# --- Chat History Management ---

def add_message_to_history(session_id: str, message_type: str, content: str):
    """Adds a new message to the chat history for a given session."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO chat_history (session_id, message_type, content) VALUES (?, ?, ?)",
        (session_id, message_type, content)
    )
    conn.commit()
    conn.close()

def get_chat_history(session_id: str):
    """Retrieves the chat history for a given session and formats it for LangChain."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT message_type, content FROM chat_history WHERE session_id = ? ORDER BY id", (session_id,))
    
    history = []
    for row in cursor.fetchall():
        if row['message_type'] == 'human':
            history.append(HumanMessage(content=row['content']))
        elif row['message_type'] == 'ai':
            history.append(AIMessage(content=row['content']))
            
    conn.close()
    return history
