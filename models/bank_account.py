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
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()

        cur.execute("UPDATE accounts SET balance = balance + ? WHERE name =?", (amount, self.name))

        conn.commit()
        conn.close()

        self.log_transaction(amount, "Deposit")
        return f"Success! You deposited {amount}. Thank you."
    
    def withdraw(self, amount):
        balance = self.get_balance()

        if balance >= amount:
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()

            cur.execute("UPDATE accounts SET balance = balance - ? WHERE name = ?", (amount, self.name))

            conn.commit()
            conn.close()
            self.log_transaction(amount, "Withdraw")
            return f"Success! You withdrawed {amount}. Thank you."
        else:
            return f"Your balance {balance} is not enough"

    def export_statement(self):
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()

        cur.execute("SELECT date, transaction_type, amount FROM transactions WHERE name = ?",(self.name,))

        data = cur.fetchall()

        #conn.commit()
        conn.close()

        if not data:
            return "There is No transaction to print"
        
        lines = []
        lines.append(f"Statement for: {self.name}")
        lines.append("-" * 50)
        lines.append(f"{'DATE':<20} | {'TYPE':<15} | {'AMOUNT':<10}")
        lines.append("-" * 50)

        for row in data:
            date, trans_type, amount = row
            lines.append(f"{date:<20} | {trans_type:<15} | {amount:<10.2f}")
            lines.append("-" * 50)

        file_name = f"{self.name}_statement.txt"
        full_content = "\n".join(lines)

        with open(file_name, "w", encoding="utf-8") as file:
            file.write(full_content)
        
        return f"Your Statement has been printed in {file_name}"
