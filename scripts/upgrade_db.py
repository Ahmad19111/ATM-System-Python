import sqlite3
import os

current_dir = os.path.dirname(__file__)
root_dir = os.path.dirname(current_dir)
db_path = os.path.join(root_dir, "bank.db")

conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS transactions  (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    amount REAL,
    transaction_type TEXT,
    date TEXT
)
""")

conn.commit()
conn.close()

print("Success, archiv have added")