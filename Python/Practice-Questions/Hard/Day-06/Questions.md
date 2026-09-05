🔴 HARD
7. 🔥 AI Dataset Cleaner

Imagine you receive this messy dataset:

data = [
    [" Prathyush ", "24", "India"],
    ["RAHUL", "27", "india"],
    [" sneha", "22", "INDIA"],
    ["Anil ", "25", "India"]
]

Your goal is to produce:

[
    ["Prathyush", 24, "India"],
    ["Rahul", 27, "India"],
    ["Sneha", 22, "India"],
    ["Anil", 25, "India"]
]

Notice:

Names have inconsistent spaces/capitalization.
Ages are strings and need to become numbers.
Countries have inconsistent capitalization.
Challenge

You must process the entire 2D list programmatically.

Don't manually modify individual rows.

Think:
2D list
   ↓
row
   ↓
individual value
   ↓
clean/convert
   ↓
store result

This is very close to the type of thinking you'll eventually use with Pandas.

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

9. 🔥🔥🔥 Mini AI Dataset Engine

This is your biggest challenge so far.

Imagine you receive the following dataset:

dataset = [
    ["Prathyush", 24, 85],
    ["Rahul", 27, 72],
    ["Sneha", 22, 91],
    ["Anil", 25, 64],
    ["Kiran", 23, 88]
]

Each row contains:

[Name, Age, Score]

Your program must analyze the dataset.

Part 1 — Basic statistics

Display:

Number of students: 5
Average score: ...
Highest score: ...
Lowest score: ...
Part 2 — Classification

Determine how many students fall into:

90+       → Excellent
75–89     → Good
60–74     → Average
Below 60  → Needs Improvement

Display:

Excellent: ...
Good: ...
Average: ...
Needs Improvement: ...
Part 3 — Find the best student

Your program should determine:

Best student: Sneha
Score: 91

Don't manually search for Sneha.

Your algorithm should work if the dataset changes.

For example:

dataset = [
    ["John", 21, 95],
    ["Alex", 25, 82],
    ["Sam", 23, 97]
]

Your program should automatically find the new best student.

Part 4 — User search

Ask:

Enter student name:

If the student exists:

Name: Rahul
Age: 27
Score: 72

If they don't:

Student not found.

Your search should be case-insensitive.

So:

rahul
RAHUL
RaHuL

should all find Rahul.

Part 5 — 🔥 Create a filtered dataset

Ask the user:

Enter minimum score:

If they enter:

80

create a new list containing only students whose score is 80 or higher.

For the original dataset:

[
    ["Prathyush", 24, 85],
    ["Sneha", 22, 91],
    ["Kiran", 23, 88]
]
Constraints

For this challenge, don't use:

Pandas
NumPy
max()
min()
sum()
set()

Use the Python concepts you've learned so far.