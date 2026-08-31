"""
1. Student Score Analyzer

Create a list containing 5 student scores:

c

Your program should display:

Scores: [72, 85, 91, 64, 78]

Highest score: 91
Lowest score: 64
Average score: 78.0
Rules

Don't use:

max()
min()
sum()

Use your own reasoning to calculate them.

Bonus: Count how many students scored above the average.
"""

student_scores = [72, 85, 91, 64, 78]

highest_score = student_scores[0]
lowest_score = student_scores[0]
average_score = 0
total_score_sum = 0
sutdents_scored_above_avg = 0


for score in student_scores:
    total_score_sum += score
    if score > highest_score:
        highest_score = score
    if score < lowest_score :
        lowest_score = score

average_score = total_score_sum / len(student_scores)

for score in student_scores:
    if score > average_score:
        sutdents_scored_above_avg += 1




print(f"Highest score: {highest_score}")
print(f"Lowest score: {lowest_score}")
print(f"Average score: {average_score}")
print(f"Students scored above average: {sutdents_scored_above_avg}")