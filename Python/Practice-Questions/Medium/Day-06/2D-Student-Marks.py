"""
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
"""
marks = [
    [80, 75, 90, 85],
    [65, 70, 72, 68],
    [92, 88, 95, 90]
]

student_averages = []

for student in marks:
    average = sum(student) / len(student)
    student_averages.append(average)

for i, average in enumerate(student_averages):
    print(f"Student {i+1} average:{average:.2f}")

best_student = student_averages[0]

for avg in student_averages:
    if avg > best_student:
        best_student = avg

print(f"Best student: Student {student_averages.index(best_student)+1}")
