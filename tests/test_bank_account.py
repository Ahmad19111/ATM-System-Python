from models.bank_account import BankAccount

def test_account_creation():
    test_name = "Max Mustermann"
    account = BankAccount(test_name)

    assert account.name == test_name