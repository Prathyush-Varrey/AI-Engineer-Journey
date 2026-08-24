"""
1. Extract the Username

Ask the user to enter an email address:

Enter email: prathyush@gmail.com

Extract and display only the username:

Username: prathyush

Constraint: Use string slicing to extract the username.

Test with at least 3 different email addresses.
"""

user_email = input("Enter Yoour Email Address :").strip()

find_astrey = user_email.find("@")

user_name_from_user_email = user_email[:find_astrey]
print(user_name_from_user_email)