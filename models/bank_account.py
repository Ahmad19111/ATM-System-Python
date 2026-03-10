import sqlite3
from datetime import datetime
from database.db_manager import DB_PATH

class BankAccount:
    def __init__(self, name):
        self.name = name

    def log_transaction(self, amount, trans_type):
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cur.execute("INSERT INTO transactions (name, amount, transaction_type, date) VALUES (?, ?, ?, ?)", (self.name, amount, trans_type, current_time))

        conn.commit()
        conn.close()

    def get_balance(self):
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()

        cur.execute("SELECT balance FROM accounts WHERE name = ?", (self.name,))

        result = cur.fetchone()

        conn.close()

        if result:
            return result[0]
        else:
            return None

    def deposit(self, amount):
        balance = self.get_balance()
        if balance is None:
            return None
        
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()

        cur.execute("UPDATE accounts SET balance = balance + ? WHERE name =?", (amount, self.name))

        conn.commit()
        conn.close()

        self.log_transaction(amount, "Deposit")
        return True
    
    def withdraw(self, amount):
        balance = self.get_balance()
        if balance is None:
            return None
        elif balance >= amount:
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()

            cur.execute("UPDATE accounts SET balance = balance - ? WHERE name = ?", (amount, self.name))

            conn.commit()
            conn.close()
            self.log_transaction(amount, "Withdraw")
            return True
        else:
            return False

    def get_statement_data(self):
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()

        cur.execute("SELECT date, transaction_type, amount FROM transactions WHERE name = ?",(self.name,))
        data = cur.fetchall()
        conn.close()

        if not data:
                return []
        
        transactions_list = []

        for row in data:
            date, transaction_type, amount = row
            transactions_list.append({"date": date, "type":transaction_type, "amount":amount })

        return transactions_list 