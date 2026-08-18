"""
3. Username Generator

Ask the user for:

First name: Prathyush
Last name: Webdev

Generate:

Username: prathyush_webdev

Your program should still produce the same style of username if the user enters:

Prathyush
WEBDEV

Think: Which string operations can make the input consistent?
"""

first_name = input("Enter your first name:").strip().lower()
last_name = input("Enter your last name:").strip().lower()

#generate username
username = first_name + "_" + last_name
print(f"Your Generated Username is : {username}")