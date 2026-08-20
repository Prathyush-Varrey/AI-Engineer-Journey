
"""
1. Distance Calculator

Ask the user for two numbers representing the starting point and ending point.

For example:

Starting point: 12
Ending point: 5

Output:

Distance: 7

Your program should produce a positive distance regardless of which number is larger.

Think: What mathematical operation/function can help you here?

"""

starting_point = int(input("Enter Starting Point :"))
ending_point = int(input("Enter Ending Point :"))

distance = abs(starting_point - ending_point)
print(f"Distance : {distance}")


