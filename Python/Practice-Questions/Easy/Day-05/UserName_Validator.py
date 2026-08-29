"""
2. Clean Username Validator

Ask the user to enter a username.

A valid username must:

Be between 5 and 15 characters
Not contain spaces
Be converted to lowercase before checking
Start with a letter

Example:

Enter username: Prathyush24

Username accepted: prathyush24

But:

Enter username: prathyush webdev

Invalid username

Don't use lists or advanced concepts.

Think: How can several conditions be combined into one decision?

solution  flow
        User Enters user name a string
                    |
        check the len of the characters (should not exceed 15 and should not be less that 5) rnage(5, 15)
                    |
        Check for spaces (if yu have spaces user name should be Invalid Username)
                    |
        if user name is valid then convert it to lowercase
                    |
        should check it starts with letter
                    |
        if it passes every check then It is avalid user name then print (username accepted : {user_name})
         if not it's invalid name
"""

user_name = input("Enter your username: ").lower()

length_username = len(user_name)
find_spaces = user_name.find(" ")

if 5<= length_username <= 15 and find_spaces == -1 and user_name[0].isalpha():
    print(f"Username accepted : {user_name}")
else:
    print("Invalid username")