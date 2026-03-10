import pytest
from fastapi.testclient import TestClient
from api_server import app

# Create a dummy client to test the server
client = TestClient(app)

# 1. Test the root endpoint (Server status)
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Bank API!", "status": "Online"}

# 2. Test checking balance for a non-existent account
# Note: Based on the current api_server.py, this returns 200 OK with an error message in JSON
def test_get_balance_not_found():
    response = client.get("/balance/GhostUser123")
    assert response.status_code == 200
    assert response.json() == {"error": "Account not found", "username": "GhostUser123"}

# 3. Test depositing money to a non-existent account (Should return 404)
def test_deposit_account_not_found():
    response = client.post("/deposit", json={"username": "GhostUser123", "amount": 100})
    assert response.status_code == 404
    assert response.json()["detail"] == "Account 'GhostUser123'not found."

# 4. Test withdrawing money from a non-existent account (Should return 404)
def test_withdraw_account_not_found():
    response = client.post("/withdraw", json={"username": "GhostUser123", "amount": 50})
    assert response.status_code == 404
    assert response.json()["detail"] == "Account 'GhostUser123'not found."

# 5. Test withdrawing more money than the current balance (Should return 400)
def test_withdraw_insufficient_funds():
    # Step A: Deposit a small amount to create the account and set a balance
    client.post("/deposit", json={"username": "PoorUser", "amount": 50})
    
    # Step B: Try to withdraw a much larger amount
    response = client.post("/withdraw", json={"username": "Ahmad", "amount": 9999})
    
    # Step C: Assert that the server blocks it and returns 400 Bad Request
    assert response.status_code == 400
    assert response.json()["detail"] == "Insufficient funds"

# 6. Test getting statement for an account with no transactions
def test_get_statement_empty():
    response = client.get("/statement/GhostUser123")
    assert response.status_code == 200
    assert response.json() == {"message": "No transactions found"}