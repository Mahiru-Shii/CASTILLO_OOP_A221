account_name = "Juan Dela Cruz"
balance = 10000.00


# TODO 1: Create welcome_user(name)
def welcome_user(name):
    print("==============================")
    print("  PYTHON CLI ATM by CASTILLO ")
    print(f"  Welcome, {name}!")
    print("==============================")


# TODO 2: Create check_balance(balance)
def check_balance(balance):
    print(f"Current Balance: ₱{balance:.2f}")


# TODO 3: Create deposit_money(current_balance, amount)
def deposit_money(current_balance, amount):
    return current_balance + amount


# TODO 4: Create save_transaction(name, transaction, amount)
def save_transaction(name, transaction, amount):
    file = open("transactions.txt", "w")
    file.write(f"Account: {name}\n")
    file.write(f"Transaction: {transaction}\n")
    file.write(f"Amount: ₱{amount}")
    file.close()


# TODO 5: Create view_history()
def view_history():
    file = open("transactions.txt", "r")
    lines = file.readlines()
    file.close()

    print("===== TRANSACTION HISTORY =====")

    for line in lines:
        print(line.strip())


# TODO 6: Create analyze_transactions()
def analyze_transactions():
    file = open("transactions.txt", "r")
    content = file.read()
    file.close()

    deposit_count = content.count("Deposit")
    first_deposit = content.find("Deposit")

    print("===== TRANSACTION ANALYSIS =====")
    print(f"Total Deposits: {deposit_count}")
    print(f"First Deposit Index: {first_deposit}")


welcome_user(account_name)

print()
print("===== ATM MENU by LASTNAME =====")
print("1. Check Balance")
print("2. Deposit")
print("3. View History")
print("4. Analyze Transactions")

choice = input("Choose option: ")


# TODO 7: Check Balance
if choice == "1":

    # Call check_balance()
    check_balance(balance)


# TODO 8: Deposit
elif choice == "2":

    deposit = float(input("Enter deposit amount: "))

    if deposit > 0:

        # TODO 9: Update the balance using deposit_money()
        balance = deposit_money(balance, deposit)

        # TODO 10: Save the transaction
        save_transaction(account_name, "Deposit", deposit)

        print("Deposit successful.")
        print(f"New Balance: ₱{balance:.2f}")

    else:
        print("Invalid deposit amount.")


# TODO 11: View History
elif choice == "3":
    view_history()


# TODO 12: Analyze Transactions
elif choice == "4":
    analyze_transactions()


else:
    print("Invalid option.")

""" 
######### Learning Signature ######### 
Programmed by: Castillo, Lucky James S.
Date Submitted: August 29, 2026
 
Program Description: This program ATM CLI.
Reflection: I learned the use of FILE.
 
AI Usage
[/] No AI Assistance – Completed independently without AI.
[ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""