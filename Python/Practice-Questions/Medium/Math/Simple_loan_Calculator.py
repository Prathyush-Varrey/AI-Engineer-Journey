"""
6. Simple Loan Calculator

Ask the user for:

Loan amount
Annual interest rate
Number of years

Calculate the simple interest:

Simple Interest = Principal × Rate × Time

The user enters the rate as a percentage.

Example:

Loan amount: 50000
Annual interest rate: 8
Years: 3


Interest: 12000
Total repayment: 62000

Your program should calculate both the interest and the final repayment amount.

Challenge: Make sure the percentage is converted correctly before performing the calculation.
"""


loan_amount = int(input("Enter Your Loan Amount :"))
annual_interest_rate = float(input("Enter Annual Interest Rate Quoted :"))
number_of_years = int(input("Enter Total Years :"))

annual_interest_rate_decimal = annual_interest_rate /100

simple_interest = loan_amount * annual_interest_rate_decimal * number_of_years
Total_repayment = loan_amount + simple_interest
print(f"Loan amount: {loan_amount}")
print(f"Annual interest rate: {annual_interest_rate}")
print(f"Years: {number_of_years}")
print(f"Interest: {simple_interest}")
print(f"Total repayment: {Total_repayment}")