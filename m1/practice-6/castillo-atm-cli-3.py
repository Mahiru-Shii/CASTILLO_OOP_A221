account_name = "Juan Dela Cruz"
transaction_type = "Deposit"
amount = 3000

# TODO 1: Open transactions.txt using write mode
file = open("transactions.txt", "w")

# TODO 2: Write the account name
file.write(f"Account: {account_name}\n")

# TODO 3: Write the transaction type
file.write(f"Transaction: {transaction_type}\n")

# TODO 4: Write the amount
file.write(f"Amount: ₱{amount}")

# TODO 5: Close the file
file.close()

print("Transaction saved successfully.")

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