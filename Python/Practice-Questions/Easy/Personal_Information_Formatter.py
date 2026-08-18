"""
Personal Information Formatter

Ask the user for:

First name
Last name
Age

Then produce an output like:

Hello Prathyush, you are 24 years old.

Constraint: The user may accidentally enter spaces before or after their name. Your program should handle that.
"""
first_name = str(input("Enter your first name:").strip())
last_name = str(input("Enter your Last name:").strip())
age = input("Enter Your age:").strip()

age = int(age)
first_name = first_name.capitalize()
last_name = last_name.capitalize()

print(f"Hello {first_name}, you are {age} years old")