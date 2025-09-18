import sqlite3

# Connect to database (creates file if not exists)
def get_db():
    conn = sqlite3.connect("expenses.db")  # make sure the name matches everywhere
    conn.row_factory = sqlite3.Row  # lets us access columns by name
    return conn

# Initialize database tables
def init_db():
    conn = get_db()
    cursor = conn.cursor()

    # Expenses table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT,
            date TEXT
        )
    """)

    # Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    conn.commit()  # <--- IMPORTANT: actually save changes
    conn.close()
