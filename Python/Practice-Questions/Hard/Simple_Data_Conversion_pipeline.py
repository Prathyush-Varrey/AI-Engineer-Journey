"""
Build a Simple Data Conversion Pipeline

A user enters their details:

Name: Prathyush
Age: 24
Height: 5.9

Your program should produce:

Name: PRATHYUSH
Age next year: 25
Height in centimeters: 179.83

You need to figure out:

Which inputs need conversion?
What mathematical operation is required?
Which string operation produces the required name format?
How do you combine everything into the final output?

Don't search for the solution. Try to break the problem into smaller steps first.

Approach :
            Ask user details
                |
            convert the name to upper case and age to integer and height to float
                |
            conter Height which is in feet to centimeters by multiplying with 30.48
                |
            Display the details

"""

user_name = input("Enter Your Name :").strip().upper()
user_age = int(input("Enter Your Age :").strip())
user_height = float(input("Enter Your Height (in feet) :").strip())

user_age_next_year = user_age + 1
user_height_cm = user_height * 30.48

print(f"Name : {user_name}")
print(f"Age next year : {user_age_next_year}")
print(f"Height in centimeters : {user_height}")