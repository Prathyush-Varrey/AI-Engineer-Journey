"""
2. Search Through a List

Given:

numbers = [12, 45, 7, 23, 45, 89, 31, 45]

Ask the user for a number.

For example:

Enter number to search: 45

Output:

45 found 3 times.

If they enter:

Enter number to search: 100

Output:

100 was not found.

Think: How can you examine every element and keep track of how many times something appears?
"""

numbers = [12, 45, 7, 23, 45, 89, 31, 45]

number_to_search = int(input("Enter number to search: "))

repeated = 0
isfound = False

for nums in numbers:
    if nums == number_to_search:
        isfound = True
        repeated += 1


if isfound :
    print(f"{number_to_search} found {repeated} times.")
else:
    print(f"{number_to_search} not found")