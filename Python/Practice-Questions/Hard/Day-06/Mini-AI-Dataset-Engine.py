"""
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
"""


dataset = [
    ["Prathyush", 24, 85],
    ["Rahul", 27, 72],
    ["Sneha", 22, 91],
    ["Anil", 25, 64],
    ["Kiran", 23, 88]
]

"""
Part 1 — Basic statistics

Display:

Number of students: 5
Average score: ...
Highest score: ...
Lowest score: ...
"""
number_of_students = len(dataset)
average_score = 0
highest_score = dataset[0][2]
lowest_score = dataset[0][2]
total_score = 0

"""
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
"""

excellent = 0
good = 0
average = 0
needs_improvement = 0

for student in dataset:
    total_score += student[2]

    if student[2] > highest_score:
        highest_score = student[2]
    if student[2] < lowest_score:
        lowest_score = student[2]

    if student[2] >= 90:
        excellent += 1
    elif student[2] >= 75:
        good +=1
    elif student[2] >= 60:
        average += 1
    else:
        needs_improvement += 1

average_score = total_score / number_of_students 
print("Part 1 — Basic statistics")
print(f"Number of students : {number_of_students}")
print(f"Average score: {average_score}")
print(f"Highest score: {highest_score}")
print(f"Lowest score: {lowest_score}")

#Part 2 classification
print()
print("Part 2 classification")
print(f"Excellent : {excellent}")
print(f"Good: {good}")
print(f"Average: {average}")
print(f"Needs Improvement: {needs_improvement}")


"""
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
"""
best_student = dataset[0][0]
best_student_score = dataset[0][2]
for student in dataset:
    if student[2] > best_student_score:
        best_student_score = student[2]
        best_student = student[0]

print(f"Best student: {best_student}")
print(f"Score: {best_student_score}")

"""
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
"""

student_name = input("Enter student name: ").strip().capitalize()
student_found = False

print()
print("Part 4 — User search")
for student in dataset:
    if student[0] == student_name:
        print(f"Name : {student[0]}")
        print(f"Age: {student[1]}")
        print(f"Score: {student[2]}")
        student_found = True
        break

if not student_found:
    print("Student not found.")

"""
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
"""
print()
print("Part 5 — 🔥 Create a filtered dataset")
minimum_score = int(input("Enter minimum score: "))

filtered_list = []

for student in dataset:
    if student[2] >= minimum_score:
        filtered_list.append(student)

print(f"For the original dataset: {filtered_list}")