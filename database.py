import sqlite3

def init_db():
    conn = sqlite3.connect("finance.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT,
                    description TEXT,
                    amount REAL,
                    category TEXT
                 )''')
    conn.commit()
    conn.close()

init_db()
