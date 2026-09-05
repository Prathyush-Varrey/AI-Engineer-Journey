"""
8. 🔥🔥 Matrix Analyzer

Given:

matrix = [
    [3, 7, 2],
    [9, 1, 5],
    [4, 8, 6]
]

Your program must calculate:

A. Total of all numbers
Total: ...
B. Largest number
Largest: ...
C. Smallest number
Smallest: ...
D. Number of even values
Even numbers: ...
E. Number of odd values
Odd numbers: ...
F. Row totals
Row 1 total: ...
Row 2 total: ...
Row 3 total: ...
G. Column totals
Column 1 total: ...
Column 2 total: ...
Column 3 total: ...
Constraints

Don't use:

sum()
min()
max()

And don't manually calculate each row/column.

🔥 Think carefully

Rows are straightforward because your 2D list is organized by rows.

Columns require a different way of thinking.

Ask yourself:

If I'm currently looking at column 2, how do I reach column 2 inside every row?

That's the important reasoning challenge.

"""

matrix = [
    [3, 7, 2],
    [9, 1, 5],
    [4, 8, 6]
]

# A. Total of all numbers Total: ...
total = 0

for row in matrix:
    for num in row:
        total+= num
print(total)

"""
B. Largest number
Largest: ...
C. Smallest number
Smallest: ...
"""
largest_num = matrix[0] [0]
smallest_num = matrix[0] [0]
for row in matrix:
    for num in row:
        if num < largest_num:
            largest_num = num
        if num > smallest_num:
            smallest_num = num

print(largest_num)
print(smallest_num)

"""
D. Number of even values
Even numbers: ...
E. Number of odd values
Odd numbers: ...
"""

even_nums = 0
odd_nums = 0

for row in matrix:
    for num in row:
        if num % 2 ==0:
            even_nums +=1
        else:
            odd_nums +=1
print(even_nums)
print(odd_nums)

"""
F. Row totals
Row 1 total: ...
Row 2 total: ...
Row 3 total: ...
"""

rows_sum = []

for row in matrix:
    current_sum = 0
    for num in row:
        current_sum += num
    rows_sum.append(current_sum)

print(f"Row 1 total : {rows_sum[0]}")
print(f"Row 2 total : {rows_sum[1]}")
print(f"Row 3 total : {rows_sum[2]}")

"""
G. Column totals
Column 1 total: ...
Column 2 total: ...
Column 3 total: ...
"""

col_sum = []

num_rows = len(matrix)
num_col = len(matrix[0])

for col in range(num_col):
    current_sum = 0
    for row in range(num_rows):
        current_sum += matrix[row][col]
    col_sum.append(current_sum)

print(f"Column 1 total: {col_sum[0]}")
print(f"Column 2 total: {col_sum[1]}")
print(f"Column 3 total: {col_sum[2]}")
