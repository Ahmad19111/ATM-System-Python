import sqlite3
import os

current_dir = os.path.dirname(__file__)
db_path = os.path.join(current_dir, "bank.db")

conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute(" INSERT INTO accounts (name, Balance) VALUES (?, ?)", ('Ahmad', 1000.50))

conn.commit()
conn.close()