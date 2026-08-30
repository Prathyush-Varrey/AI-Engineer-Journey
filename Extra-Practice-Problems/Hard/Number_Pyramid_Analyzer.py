"""
8. 🔥🔥 Number Pyramid Analyzer

Create a program that asks:

Enter number of rows: 5

and produces:

1
12
123
1234
12345

Then modify the logic to produce:

1
22
333
4444
55555

Now comes the actual challenge.

Ask the user for the number of rows and generate:

1
22
333
4444
55555
...

for any number of rows.

If the user enters:

7

you should automatically produce seven rows.

Extra challenge

Create:

12345
1234
123
12
1

for any number of rows.

Don't create separate code for each possible row count.

Your job is to discover the relationship between:

row number ↔ number of repetitions ↔ value being printed
"""

rows = int(input("Enter Number of Rows: "))

#outter loop works on rows
for i in range(rows):
    #inner loop prints the nums
    for j in range(i+1):
        print(j + 1, end="")
    print()

print()

#outter loop works on rows
for i in range(rows):
    #inner loop prints the nums
    for j in range(i+1):
        print(i + 1, end="")
    print()

print()

#reverse pyramid
for i in range(rows):
    for j in range(0, rows - i):
        print(j + 1, end="")
    print()