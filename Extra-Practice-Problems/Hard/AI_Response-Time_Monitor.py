"""
7. 🔥 AI Response-Time Monitor

You're monitoring an AI API.

Ask:

How many requests were made?

For each request, ask for the response time.

Example:

How many requests? 7

Request 1: 120
Request 2: 85
Request 3: 340
Request 4: 92
Request 5: 210
Request 6: 67
Request 7: 180

Your program should calculate:

Total requests: 7
Average response time: 156.28 ms
Fastest response: 67 ms
Slowest response: 340 ms
Requests above 200 ms: 2
Requests below 100 ms: 3
Constraints

Don't use:

list
min()
max()
sum()

You've already encountered this problem in the previous set, but this time add one more requirement:

Display a performance rating:

Average < 100    → Excellent
Average 100–200  → Good
Average > 200    → Needs Improvement

Think carefully about the boundary values.

What happens at exactly:
100
200
"""

request_count_from_API = int(input("How many requests were made?: "))
average_response_time = 0
fastest_response_time = None
slowest_response_time = None
request_above_200ms = 0
request_below_100ms = 0
total_response_time = 0
performance = None
for i in range(request_count_from_API):
    request = int(input(f"Rquest {i +1}: "))

    total_response_time += request

    #fastest and slowest requests 
    if fastest_response_time is None and slowest_response_time is None:
        fastest_response_time = request
        slowest_response_time = request
    else:
        if request < fastest_response_time:
            fastest_response_time = request
        if request > slowest_response_time:
            slowest_response_time = request
    #above 200 and below 100
    if request > 200:
        request_above_200ms +=1
    if request < 100:
        request_below_100ms += 1

# average response time 
average_response_time = total_response_time / request_count_from_API

if average_response_time < 100:
    performance = "Excellent"
elif average_response_time <= 200:
    performance = "Good"
else:
    performance = "Needs Improvement"

print(f"Total requests : {request_count_from_API}")
print(f"Average response time: {average_response_time}")
print(f"Fastest response: {fastest_response_time}")
print(f"Slowest response: {slowest_response_time}")
print(f"Requests above 200 ms: {request_above_200ms}")
print(f"Requests below 100 ms: {request_below_100ms}")
print(f"{performance}")