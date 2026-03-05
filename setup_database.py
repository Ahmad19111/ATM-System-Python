import sqlite3
import os

current_dir = os.path.dirname(__file__)
db_path = os.path.join(current_dir, "bank.db")

conn = sqlite3.connect(db_path)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS accounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    balance REAL
)""")

conn.commit()
conn.close()

