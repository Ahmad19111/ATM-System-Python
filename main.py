from models.bank_account import BankAccount

current_user = None
while True:
    name_input = input("Enter your name plase to login:")
    if not name_input.replace(" ", "").isalpha():
        print("Plase enter a valid name(letters only, no numbers).")
        continue
    temp_account = BankAccount(name_input)
    balance = temp_account.get_balance()

    if balance is None:
        print(f"Sorry {name_input} you don't have an account. Try again.")
    else:
        print(f"Hello {name_input}, Welcome back!")
        current_user = temp_account
        break

while True:
    try:
        print("\n--- MENU ---")
        print("1. Show balance \n2. Deposit \n3. Withdraw \n4. Print Statment \n5. Exit")
        answer = int(input("Plase enter your chois: "))
        
        if answer == 1:
            print(f"Your balance is: {current_user.get_balance()}")

        elif answer == 2:
            amount = float(input("How match mony you want to deposit: "))
            current_user.deposit(amount)
            print(f"You have diposit: {amount}, your balance now is: {current_user.get_balance()}.")
        
        elif answer == 3:
            amount = float(input("How match mony you want to withdraw: "))
            
            print(current_user.withdraw(amount))
            print(f"Your balance now is: {current_user.get_balance()}")

        elif answer == 4:
            print(current_user.export_statement())

        elif answer == 5:
            break

        else:
            print("Plase enter just a valid number: 1, 2, 3, 4")
            continue


    except ValueError:
        print("Plase enter just a valid number: 1, 2, 3, 4")