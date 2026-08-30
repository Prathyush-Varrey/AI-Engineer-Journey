"""
5. Login System with Validation

Build a simple login system.

Predefined:

correct_username = "prathyush"
correct_password = "python123"

Ask the user for username and password.

The program should allow 3 attempts.

But now introduce these rules:

Username should be case-insensitive.
Leading/trailing spaces should be ignored.
Password should be case-sensitive.
If username is correct but password is wrong, say "Wrong password."
If username is wrong, say "User not found."

Example:

Username:   PRATHYUSH
Password: python123

Login successful!
Reasoning challenge

Don't treat username and password as one giant condition immediately.

Think about the different states the program can encounter.
"""

correct_username = "prathyush"
correct_password = "python123"

attempts = 3
while attempts >0:
    user_entered_username = input("Enter your User Name: ").strip().lower()
    user_entered_password = input("Enter your Password: ").strip()

    if user_entered_username == correct_username:
        if user_entered_password == correct_password:
            print("Login Successful !")
            break
        else:
            print("Wrong Password.")
    else:
        print("User not found")
    attempts -= 1
    if attempts >0:
        print(f"Attempts remaining : {attempts}")