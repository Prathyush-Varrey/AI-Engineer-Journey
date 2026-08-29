"""
4. Password Strength Analyzer

Ask the user to enter a password.

Your program should check whether the password satisfies all of these:

At least 8 characters
Contains at least one uppercase letter
Contains at least one lowercase letter
Contains at least one number

Then display:

Password: ********

Strength: Strong

If one or more requirements aren't met, tell the user which requirements are missing.

Important constraint

You cannot use regular expressions, lists, or libraries.

Use the Python concepts you've learned so far.

Think carefully: How can a loop inspect the password one character at a time?
"""

user_password = input("Enter Your Password : ").strip()
has_uppercase = False
has_lowercase = False
has_number = False
length_userpassword = len(user_password)

for i in user_password:
    if i.isupper():
        has_uppercase = True
    elif i.islower():
        has_lowercase = True
    elif i.isdigit():
        has_number = True

if length_userpassword >= 8 and has_number and has_lowercase and has_uppercase :
    print(f"Password : {'*' * length_userpassword}")
    print("Strength : Strong")
else:
    print(f"Password : {'*' * length_userpassword}")
    print("Strength : Weak")
    if length_userpassword < 8 :
        print("Missing : At least 8 characters ")
    if not has_uppercase:
        print("Missing : At least 1 upper case letter")
    if not has_lowercase:
        print("Missing : At least 1 lower case letter")
    if not has_number:
        print("Missing : At least 1 number")
        