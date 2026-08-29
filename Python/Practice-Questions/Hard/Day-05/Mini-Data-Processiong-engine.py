"""
9. 🔥🔥 Mini Data Processing Engine

This is your most important problem today.

Imagine an AI system sends you a series of numbers representing model response times in milliseconds.

Ask the user:

How many response times do you want to enter?

Suppose they enter:

5

Then repeatedly ask:

Enter response time 1: 120
Enter response time 2: 85
Enter response time 3: 230
Enter response time 4: 95
Enter response time 5: 310

Your program must determine:

Total response time
Average response time
Fastest response
Slowest response
Number of responses above 200 ms
Number of responses below 100 ms

Then produce something like:

Total: 840 ms
Average: 168 ms
Fastest: 85 ms
Slowest: 310 ms
Above 200 ms: 2
Below 100 ms: 1
🔥 Constraints

You are not allowed to use:

Lists
min()
max()
sum()
NumPy
Pandas

You need to reason your way through the problem using the concepts you've learned.

Think before coding

Ask yourself:

How can I remember the fastest value while I'm still receiving numbers?

How can I remember the slowest value?

How can I count values satisfying a condition?

How can I calculate the average without storing every number?

This problem is deliberately designed to make you think like a programmer rather than just use Python functions.
"""

import math
response_cycles = int(input("How many response times do you want to enter? : "))
total_time = 0
fastest_val = None
slowest_val = None
above_200 = 0
below_100 = 0

for i in range(response_cycles):
    response_time = int(input(f"Enter Response time {i + 1} : "))

    #total
    total_time += response_time

    #fastest and slowest value
    if fastest_val is None  and slowest_val is None:
        fastest_val = response_time
        slowest_val = response_time
    else :
        if response_time < fastest_val:
            fastest_val = response_time

        if response_time > slowest_val:
            slowest_val = response_time

    #above  200 
    if response_time > 200:
        above_200 += 1

    if response_time < 100:
        below_100 += 1

avg_response = math.floor(total_time / response_cycles
)

print(f"Total: {total_time} ms")
print(f"Average: {avg_response} ms")
print(f"Fastest: {fastest_val} ms")
print(f"Slowest: {slowest_val} ms")
print(f"Above: {above_200} ")
print(f"Below: {below_100}")