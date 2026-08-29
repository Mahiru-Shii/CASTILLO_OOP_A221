balance = 10000.00
service_fee = 18.00
withdrawal_limit = 10000.00

withdraw = float(input("Enter withdrawal amount: "))

# TODO 1: Calculate the total deduction
# Total deduction = withdrawal + service fee
total_deduction = withdraw + service_fee

# TODO 2: Check if the withdrawal is valid
# It must be greater than 0
# It must not exceed the withdrawal limit
# The total deduction must not exceed the balance
if withdraw > 0 and withdraw <= withdrawal_limit and total_deduction <= balance:

    # TODO 3: Deduct the total amount from the balance
    balance -= total_deduction

    print("Withdrawal successful.")
    print(f"Withdrawal Amount: ₱{withdraw:.2f}")
    print(f"Service Fee: ₱{service_fee:.2f}")
    print(f"Total Deduction: ₱{total_deduction:.2f}")
    print(f"Remaining Balance: ₱{balance:.2f}")

else:
    print("Withdrawal denied.")

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