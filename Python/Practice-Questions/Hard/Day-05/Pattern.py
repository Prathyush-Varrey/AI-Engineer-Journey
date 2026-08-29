"""
8. 🔥 Pattern Reasoning

Use nested for loops to produce this:

*
**
***
****
*****

Then modify your program to produce:

*****
****
***
**
*

Then produce:

1
12
123
1234
12345
But here's the actual challenge:

Don't just copy three separate solutions.

Build your thinking around:

What controls the number of rows?
What controls the number of characters/numbers inside each row?

Once you understand that relationship, try:

1
22
333
4444
55555

This is your first real nested-loop reasoning
"""

rows = int(input("Enter Number of rows required : "))
#columns = int(input("Enter Number of columns required : "))


for i in range (rows):

    for j in range(i + 1):
        print(i + 1, end = "")
    print()
   