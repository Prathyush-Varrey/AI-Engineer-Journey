"""
3. Sum of Numbers in a Range

Ask the user for two numbers:

Start: 5
End: 10

Calculate:

5 + 6 + 7 + 8 + 9 + 10 = 45

Output:

Sum: 45

The user can enter the numbers in either order.

For example:

Start: 10
End: 5

should still calculate the same range.

Focus: for loop + math + conditions.
"""

start_num = int(input("Enter Starting Number : "))
end_num = int(input("Enter Ending Number : "))
total = 0
if start_num > end_num:
    for i in range(start_num, end_num -1 , -1):
        total = total + i
else :
    for i in range(start_num, end_num + 1):
        total = total + i

print(total)