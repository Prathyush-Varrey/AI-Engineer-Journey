"""
4. Remove Duplicates — Without set()

Given:

numbers = [4, 7, 4, 9, 7, 2, 9, 1, 4]

Create a new list containing only unique values:

[4, 7, 9, 2, 1]
Constraint

You cannot use set().

You need to reason about:

"Have I already seen this value?"

This is a very useful pattern in data processing.
"""

numbers = [4, 7, 4, 9, 7, 2, 9, 1, 4]

unique_nums = []

for num in numbers:
    if num not in unique_nums:
        unique_nums.append(num)

print(unique_nums)