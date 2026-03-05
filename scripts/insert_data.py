import sqlite3
import os

current_dir = os.path.dirname(__file__)
root_dir = os.path.dirname(current_dir)
db_path = os.path.join(root_dir, "bank.db")

conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute(" INSERT INTO accounts (name, Balance) VALUES (?, ?)", ('Ahmad', 1000.50))

conn.commit()
conn.close()