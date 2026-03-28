# IMPORTS
import sqlite3


# DATABASE SETUP
DB_PATH= "taskmanager.db"

def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

def init_db():
    conn= get_connection()
    cur= conn.cursor()

    cur.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id              INTEGER   PRIMARY KEY AUTOINCREMENT,
                    title           TEXT    NOT NULL,
                    description     TEXT,
                    priority        TEXT    DEFAULT 'Medium',
                    status          TEXT    DEFAULT 'Pending',
                    due_date        TEXT,
                    created_at      TEXT    DEFAULT CURRENT_TIMESTAMP
                )
        """)