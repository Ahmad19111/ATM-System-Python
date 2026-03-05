import sqlite3
import os

current_dir = os.path.dirname(__file__)
db_path = os.path.join(current_dir, "bank.db")

conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute("SELECT * FROM accounts")

rows = cur.fetchall()

for row in rows:
    print (row)

conn.close()