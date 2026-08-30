"""
9. 🔥🔥🔥 Mini AI Data Processing Engine

This is the most important problem in this set.

Imagine you're receiving numerical data from an AI system.

Ask:

How many values do you want to analyze?

Suppose:

5

Then:

Enter value 1: 12
Enter value 2: 7
Enter value 3: 25
Enter value 4: 4
Enter value 5: 18

Your program should calculate:

Basic statistics
Total: 66
Average: 13.2
Largest: 25
Smallest: 4
Classification
Positive values: 5
Negative values: 0
Zero values: 0
Even values: 3
Odd values: 2
Threshold analysis

Ask the user:

Enter threshold: 10

Then:

Values above threshold: 25, 18, 12
Values below threshold: 7, 4
But here are the constraints 🔥

You cannot use:

Lists
Tuples
Sets
Dictionaries
min()
max()
sum()

You must solve it using the concepts you've learned so far.
"""

values_to_analyze = int(input("How many values do you want to analyze? "))

#needs
#basic stats
total = 0
avgerage = 0
largest = None
smallest = None

#classifications
num_of_positiveval = 0
num_of_negativeval = 0
zero_val = 0
num_even_val = 0
num_odd_val = 0


#threshold analysis
threshold = int(input("Enter threshold: "))

values_below_threshold = ""
values_above_threshold = ""

for i in range(values_to_analyze):
    values = int(input(f"Enter values {i + 1}: "))

    total += values

    #largest and smallest 
    if largest is None and smallest is None:
        largest = values
        smallest = values
    else:
        if values > largest:
            largest = values
        if values < smallest:
            smallest = values

    #psotive , negitive and zero count
    if values > 0:
        num_of_positiveval +=1
    elif values < 0:
        num_of_negativeval += 1
    else:
        zero_val += 1

    # even and odd counts
    if values % 2 == 0:
        num_even_val += 1
    else:
        num_odd_val += 1

    #threshold analysis
    if values > threshold:
        values_above_threshold += str(values) + ", "
    else:
        values_below_threshold += str(values) + ", "

avgerage = total / values_to_analyze


#basic stats 
print(f"Total: {total}")
print(f"Average: {avgerage}")
print(f"Largest: {largest}")
print(f"Smallest: {smallest}")


#classification
print(f"Positive values: {num_of_positiveval}")
print(f"Negative values: {num_of_negativeval}")
print(f"Zero values: {zero_val}")
print(f"Even values: {num_even_val}")
print(f"Odd values: {num_odd_val}")

#threshold analysis
print(f"Values above threshold: {values_above_threshold}")
print(f"Values below threshold: {values_below_threshold}")