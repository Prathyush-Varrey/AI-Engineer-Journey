"""
2. Password Attempt System

Create a program with a predefined password:

correct_password = "python123"

Give the user 3 attempts to enter it.

Example:

Enter password: hello
Incorrect password.

Enter password: python
Incorrect password.

Enter password: python123
Access granted!

If all three attempts fail:

Account locked.
Think about:
What needs to repeat?
When should the loop stop?
What variable needs to remember the number of attempts?
"""

predefined_passowrd = "python123"

num_of_attempts = 3

for i in range(num_of_attempts):
    user_entered_password = input("Enter Password :")


    if user_entered_password == predefined_passowrd:
            print("Access granted!")
            break
    else:
            print("Incorrect password.")
else:
    print("Account locked.")

