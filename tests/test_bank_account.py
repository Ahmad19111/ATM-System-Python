import pytest
import sqlite3
from models.bank_account import BankAccount

@pytest.fixture
def setup_dummy_db(monkeypatch, tmp_path):
    dummy_db_path = tmp_path/"dummy_bank.db"
    monkeypatch.setattr("models.bank_account.DB_PATH", str(dummy_db_path))

    conn = sqlite3.connect(str(dummy_db_path))
    conn.execute("CREATE TABLE accounts (id INTEGER PRIMARY KEY, name TEXT, balance REAL)")
    conn.execute("CREATE TABLE transactions (id INTEGER PRIMARY KEY, name TEXT, amount REAL, transaction_type TEXT, date TEXT)")
    conn.execute("INSERT INTO accounts (name, balance) VALUES ('Max', 500.0)")
    conn.commit()
    conn.close()

def test_account_creation():
    account = BankAccount("Max")

    assert account.name == "Max"

def test_deposit(setup_dummy_db):
    account = BankAccount("Max")
    result = account.deposit(100)

    assert result is True

    assert account.get_balance() == 600

def test_deposit_invalid_account(setup_dummy_db):
    account = BankAccount("GohstUser")
    result = account.deposit(100)

    assert result is None

def test_withdraw_success(setup_dummy_db):
    account = BankAccount("Max")
    result = account.withdraw(200)

    assert result is True
    assert account.get_balance() == 300.0

def test_withdraw_insufficient_funds(setup_dummy_db):
    account = BankAccount("Max")
    result = account.withdraw(600)

    assert result is False
    assert account.get_balance() == 500.0

def test_withdraw_invalid_account(setup_dummy_db):
    account = BankAccount("GhostUser")
    result = account.withdraw(100)

    assert result is None