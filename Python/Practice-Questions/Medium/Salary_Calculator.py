"""
Salary Calculator

Ask the user for:

Employee name
Monthly salary
Number of months worked

Calculate the total salary earned.

Then display:

Employee: Rahul
Monthly Salary: 25000
Months Worked: 8
Total Earned: 200000

Challenge: The salary and months come from input(). Think about what type they should become before performing the calculation.

    Approch :
             Ask user details
                |
            Convert the salary and months to integer
                |
            Calculate the total salary (monthly salary * months worked)
                |
            Display the details and total salary earned
"""

employee_name = input("Enter Employee Name as per Records :").strip()
monthly_salary = int(input("Enter Monthly Salary :"))
months_worked = float(input("Enter Number of months worked in organization :"))

#I have converted tot sal withdran to float becaue what if an employee worjked for 2.5 months then 
# the total salary will be in decimal so we need to convert it to float
total_salary_earned =( monthly_salary * months_worked)

#print(f"Employee {employee_name}, worked for {months_worked} months and earned a total salary of {total_salary_earned}")

print(f"Employee: {employee_name}")
print(f"Monthly Salary: {monthly_salary}")
print(f"Months Worked: {months_worked}")
print(f"Total Earned: {total_salary_earned}")