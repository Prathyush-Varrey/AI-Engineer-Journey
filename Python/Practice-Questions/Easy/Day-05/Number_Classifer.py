"""
1. Number Classifier

Ask the user to enter a number.
Your program should determine whether the number is:

Positive
Negative
Zero

Then, if it's positive, additionally determine whether it's even or odd.

Example:

Enter a number: 17


Positive
Odd

Test your reasoning with:

17
-8
0
24
-13

Focus: input() → type casting → if → logical reasoning.
"""

number = int(input("Enter A Numer :"))


#Checks given number is Postivie or Negitive
if number == 0:
    print("Zero")

if number > 0:
    print("Positive")
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
elif number < 0:
    print("Negitive")

