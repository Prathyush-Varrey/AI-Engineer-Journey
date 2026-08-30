"""
6. Multiplication Table Generator

Ask the user for a number:

Enter number: 7

Produce:

7 × 1 = 7
7 × 2 = 14
...
7 × 10 = 70

Then ask:

How many tables do you want?

If they enter:

3

produce tables for:

7
8
9
Challenge

Don't write three separate loops.

Think about:

What should the outer loop control?

and

What should the inner loop control?

This is your bridge into nested-loop thinking.
"""

table_number = int(input("Enter A Number: "))
num_of_tables = int(input("Enter Number of table you want: "))

for i in range(num_of_tables):
    for j in range(1, 11):
        print(f"{table_number } * {j} = {table_number * j}")
    print()
    table_number += 1