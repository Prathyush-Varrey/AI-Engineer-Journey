"""
The Number Trap

Ask the user to enter two numbers.

Then print:

Their sum
Their difference
Their product

Think carefully: input() gives you something different from what you need for mathematical operations.

Example:

Enter first number: 12
Enter second number: 5


Sum: 17
Difference: 7
Product: 60

Don't hard-code anything.
"""

first_number = int(input("Enter first number:"))
second_number = int(input("Enter second number:"))

sum_of_numbers = first_number + second_number
difference_of_numbers = first_number - second_number
product_of_numbers = first_number * second_number

print(f"Sum : {sum_of_numbers}")
print(f"Difference : {difference_of_numbers}")
print(f"Product : {product_of_numbers}")