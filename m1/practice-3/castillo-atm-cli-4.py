balance = 5000.00
minimum_balance = 500.00

withdraw = float(input("Enter withdrawal amount: "))

# Calculate remaining balance
remaining_balance = balance - withdraw

# Check if withdrawal is valid
if withdraw > 0 and remaining_balance >= minimum_balance:
    balance -= withdraw

    print("Withdrawal successful.")
    print(f"Remaining Balance: ₱{balance:.2f}")

else:
    print("Withdrawal denied.")
    print(f"Minimum balance required: ₱{minimum_balance:.2f}")

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