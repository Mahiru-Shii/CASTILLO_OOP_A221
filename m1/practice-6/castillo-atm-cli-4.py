# TODO 1: Open transactions.txt using read mode
file = open("transactions.txt", "r")

# TODO 2: Read all lines from the file
lines = file.readlines()

print("===== TRANSACTION HISTORY =====")

# TODO 3: Use a for loop to process every line
for line in lines:
    print(line.strip())

# TODO 4: Close the file
file.close()

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