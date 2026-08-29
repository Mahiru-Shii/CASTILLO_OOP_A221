account_name = "Juan Dela Cruz" 
account_number = "20260001" 
balance = 10000.00 
 
print("===== ACCOUNT INFORMATION =====") 
 
# TODO 1: Display the account name 
print(f"Name: {account_name}") 
 
# TODO 2: Display the account number 
print(f"Account Number: {account_number}") 
 
# TODO 3: Display the balance with two decimal places 
print(f"Balance: ₱{balance:.2f}") 
 
# TODO 4: Check if the balance is ₱5,000 or more 
# If true, display "Status: Active" 
# Otherwise, display "Status: Low Balance" 
 
if balance > 5000: 
  print("Status: Active") 
else: 
  print("Status: Low Balance")


""" 
######### Learning Signature ######### 
Programmed by: Castillo, Lucky James S.
Date Submitted: August 29, 2026
 
Program Description: This program ATM CLI.
Reflection: I learned if else statements.
 
AI Usage
[/] No AI Assistance – Completed independently without AI.
[ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""