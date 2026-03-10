from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models.bank_account import BankAccount

app = FastAPI()

class TransactionRequest(BaseModel):
    username: str
    amount: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the Bank API!", "status": "Online"}

@app.get("/balance/{username}")
def get_balance(username: str):

    account = BankAccount(username)

    balance = account.get_balance()

    if balance is None:
        return {"error": "Account not found", "username":username}
    
    return {"username":username, "balane": balance}

@app.post("/deposit")
def deposit_mony(request:TransactionRequest):
    account = BankAccount(request.username)
    result = account.deposit(request.amount)
    

    if result is None:
        raise HTTPException(status_code = 404, detail = f"Account '{request.username}'not found.")

    current_balance = account.get_balance()
    return {"username": request.username, "message": f"Successfully deposited {request.amount}", "balance":current_balance}

@app.post("/withdraw")
def withdraw_mony(request:TransactionRequest):
    account = BankAccount(request.username)
    result =account.withdraw(request.amount)
    
    if result is None:
        raise HTTPException(status_code = 404, detail = f"Account '{request.username}'not found.")
    elif result == False:
        raise HTTPException(status_code = 400, detail = "Insufficient funds")
    
    current_balance = account.get_balance()
    return {"username":request.username, "messge": f"Successfully withdrew {request.amount}", "balance":current_balance}

@app.get("/statement/{username}")
def get_statement(username: str):
    account = BankAccount(username)

    history_data = account.get_statement_data()

    if history_data == []:
        return {"message":"No transactions found"}
    else:
        return {"username":username, "transactions": history_data}