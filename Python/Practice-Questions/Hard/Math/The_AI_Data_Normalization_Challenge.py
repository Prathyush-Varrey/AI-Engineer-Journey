"""
9. The AI Data Normalization Challenge 🔥

Imagine you're processing a numerical value before sending it into an AI pipeline.

The user enters any number, including negative or decimal values.

Your program must produce:

Original value: -17.63
Absolute value: 17.63
Rounded value: -18
Floor value: -18
Ceiling value: -17

For another input:

Original value: 8.42
Absolute value: 8.42
Rounded value: 8
Floor value: 8
Ceiling value: 9

Build the program so it works for any numeric input.

🔥 Extra challenge

Before coding, predict the output for:

-5.2

and

5.7

without running Python.

Then write your program and see whether your reasoning was correct.
"""
import math as math
user_given_number = float(input("Enter a Number as your wish :"))
absolute_value = abs(user_given_number)
rounded_value = round(user_given_number)
floor_value = math.floor(user_given_number)
ceiling_value = math.ceil(user_given_number)
print(f"Original value: {user_given_number}")
print(f"Absolute value: {absolute_value}")
print(f"Rounded value: {rounded_value}")
print(f"Floor value: {floor_value}")
print(f"Ceiling value: {ceiling_value}")