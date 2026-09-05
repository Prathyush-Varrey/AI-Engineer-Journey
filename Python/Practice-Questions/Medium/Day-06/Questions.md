🟡 MEDIUM
4. Remove Duplicates — Without set()

Given:

numbers = [4, 7, 4, 9, 7, 2, 9, 1, 4]

Create a new list containing only unique values:

[4, 7, 9, 2, 1]
Constraint

You cannot use set().

You need to reason about:

"Have I already seen this value?"

This is a very useful pattern in data processing.

5. AI Response Data Analyzer

Imagine these are response times from an AI API:

response_times = [120, 85, 340, 92, 210, 67, 180, 450, 105]

Your program should calculate:

Total requests: 9
Average response time: ...
Fastest response: ...
Slowest response: ...

Under 100 ms: ...
100–200 ms: ...
Above 200 ms: ...

Then create a new list containing only the slow responses:

Slow responses: [340, 210, 450]
Constraints

Don't use:

min()
max()
sum()

You're now combining:

Lists + loops + conditions + calculations.

6. 2D Student Marks

You have marks for 3 students across 4 subjects:

marks = [
    [80, 75, 90, 85],
    [65, 70, 72, 68],
    [92, 88, 95, 90]
]

Each row represents one student.

Calculate:

Student 1 average: ...
Student 2 average: ...
Student 3 average: ...

Then determine:

Best student: Student 3
Challenge

Don't calculate each student's average manually.

You need to discover how the outer loop and inner loop should