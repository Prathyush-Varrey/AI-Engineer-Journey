"""
3. Reverse It

Ask the user to enter a sentence.

Example:

Enter text: Python

Output:

Reversed: nohtyP

Constraint: Use string slicing rather than a loop.
"""

user_input = input("Enter a Word :")

reversed_input = user_input[::-1]
print(f"Reversed : {reversed_input}")