"""
1. Even/Odd Counter

Ask the user how many numbers they want to enter.

Example:

How many numbers? 6

Enter number 1: 12
Enter number 2: 7
Enter number 3: 18
Enter number 4: 5
Enter number 5: 20
Enter number 6: 11

Display:

Even numbers: 3
Odd numbers: 3
Challenge

Also calculate:

Even sum: 50
Odd sum: 23

Don't use lists.
"""

range_of_nums = int(input("Enter how many numbers? : "))

even_count = 0 
sum_of_even_nums = 0
odd_count = 0 
sum_of_odd_nums = 0

for i in range(range_of_nums):
    nums = int(input(f"Enter Number {i + 1}: "))
    if nums % 2 == 0:
        even_count += 1
        sum_of_even_nums += nums
    else:
        odd_count += 1
        sum_of_odd_nums += nums
print(f"Even Numbers: {even_count}")
print(f"Odd Numbers: {odd_count}")
print(f"Even sum: {sum_of_even_nums}")
print(f"Odd sum: {sum_of_odd_nums}")