balance = 15000.00
withdrawal_limit = 10000.00

withdraw = float(input("Enter withdrawal amount: "))

# TODO 1: Check if the withdrawal is zero or negative
if withdraw <= 0:
    print("Invalid withdrawal amount.")

# TODO 2: Check if the withdrawal exceeds the balance
elif withdraw > balance:
    print("Insufficient balance.")

# TODO 3: Check if the withdrawal exceeds the ATM limit
elif withdraw > withdrawal_limit:
    print("Withdrawal exceeds the ATM limit.")

# TODO 4: Process the valid withdrawal
else:
    # Subtract the withdrawal from the balance
    balance -= withdraw

    print("Withdrawal successful.")
    print(f"Remaining Balance: ₱{balance:.2f}")

""" 
######### Learning Signature ######### 
Programmed by: Castillo, Lucky James S.
Date Submitted: August 29, 2026
 
Program Description: This program ATM CLI.
Reflection: I learned if else elif statements.
 
AI Usage
[/] No AI Assistance – Completed independently without AI.
[ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""