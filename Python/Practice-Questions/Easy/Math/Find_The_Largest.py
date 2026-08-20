"""
3. Find the Largest

Ask the user to enter three numbers.

Example:

Enter number 1: 45
Enter number 2: 82
Enter number 3: 17

Output:

Largest number: 82

Constraint: Don't use if statements yet.

"""

first_number = int(input("Enter First Number :"))
second_number = int(input("Enter Second Number :"))
third_number = int(input("Enter Third Number :"))

largest_number = max(first_number, second_number, third_number)

print(f"Largest number : {largest_number}")