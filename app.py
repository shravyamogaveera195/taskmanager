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
    
# CRUD FUNCTIONS
def add_task(title,description,priority,status,due_date):
    conn= get_connection()
    conn.execute(" INSERT INTO tasks(title,description,priority,status,due_date) VALUES (?,?,?,?,?)",
                 (title,description,priority,status,due_date))
    conn.commit(); conn.close()

def get_tasks(status_filter="ALL",priority_filter="ALL",search=""):
    conn=get_connection()
    query="SELECT * FROM tasks WHERE 1=1"
    params=[]
    if status_filter !="ALL":
        query +=" AND status = ?"
        params.append(status_filter)
    if priority_filter !="ALL":
        query +=" AND priority = ?"
        params.append(priority_filter)
    if search:
        query += "AND (title LIKE ? OR description LIKE ?)"
        params += [f"%{search}%", f"%{search}"]
    query += " ORDER BY created_at DESC"
    rows= conn.execute(query,params).fetchall()
    conn.close()
    return rows
