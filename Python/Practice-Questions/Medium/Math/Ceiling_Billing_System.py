"""
4. Ceiling Billing System

A service charges ₹120 per hour, but even a fraction of an hour counts as a full hour.

For example:

Usage: 2.1 hours

The customer must pay for:

3 hours

Ask the user for the number of hours used and calculate the bill.

Example:

Hours used: 2.1


Billable hours: 3
Total bill: ₹360

Test your program with:

0.5
1
1.01
2.0
2.99

Think carefully about which math function matches the business rule.


"""
import math as math 

num_of_hours_used = float(input("Enter Number of Hours Used:"))
charges_per_hour = 120

ceiled_hours = math.ceil(num_of_hours_used)
Total_bill = ceiled_hours * charges_per_hour
print(f"Hours used: {num_of_hours_used}")
print(f"Billable hours: {ceiled_hours}")
print(f"Total bill: {Total_bill}")