import sqlite3
from datetime import datetime

DB_NAME = "quiz_results.db"

# Initialize database and table
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            score INTEGER,
            total_questions INTEGER,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

# Insert quiz result into database
def save_result(name, email, score, total):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
        INSERT INTO results (name, email, score, total_questions, timestamp)
        VALUES (?, ?, ?, ?, ?)
    """, (name, email, score, total, timestamp))
    conn.commit()
    conn.close()
