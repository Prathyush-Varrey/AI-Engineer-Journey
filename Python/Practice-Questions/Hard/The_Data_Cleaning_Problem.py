"""
7. The Data Cleaning Problem

Imagine you're receiving customer information from a messy system.

The user enters:

Name:     prathyush WEBDEV
Age:      24
Country:   india

Your program needs to produce:

Name: Prathyush Webdev
Age: 24
Country: India

The challenge is that you don't know exactly how many spaces the user will enter.

For example, they could enter:

   PRATHYUSH WEBDEV

or

prathyush webdev

or

 PrAtHyUsH WeBdEv

Design a program that normalizes the input into a clean, readable format.

Don't worry about validating whether the person actually entered a real name.

Approach: 
            Ask user details
                |
            convert the name to title case and age to integer and country to capitalize
                |
            Display the details

"""

user_name = input("Enter Your Name :").strip().title()

#here I'm leaving age as str because we don't know if the user will enter how many spaces
user_age = input("Enter Your Age :").strip()

user_country = input("Enter Your Country :").strip().capitalize()

user_age = int(user_age)  # Convert age to integer for proper formatting
print(f"Name : {user_name}")
print(f"Age : {user_age}")
print(f"Country : {user_country}")