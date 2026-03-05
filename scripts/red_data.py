import sqlite3
import os

current_dir = os.path.dirname(__file__)
root_dir = os.path.dirname(current_dir)
db_path = os.path.join(root_dir, "bank.db")

conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute("SELECT * FROM accounts")

rows = cur.fetchall()

for row in rows:
    print (row)

conn.close()