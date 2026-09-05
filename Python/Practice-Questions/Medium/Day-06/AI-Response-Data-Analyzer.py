"""
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

"""

response_times = [120, 85, 340, 92, 210, 67, 180, 450, 105]

total_requests = len(response_times)
total_time = 0
fastest_response = None
slowest_response = None
average_response = 0
under_100 = 0
between_100_200 =0
above_200 = 0
slow_responses = []
for time in response_times:
    total_time += time

    #fastest response
    if fastest_response is None or time < fastest_response:
        fastest_response = time

    # slowst response
    if slowest_response is None or time > slowest_response:
        slowest_response = time

    # categorize response times
    if time < 100:
        under_100 +=1
    elif 100 <= time <= 200:
        between_100_200 +=1
    else:
        above_200 += 1
        slow_responses.append(time)


average_response = total_time / total_requests

print(f"Total requests: {total_requests}")
print(f"Average response time: {average_response:.2f} ms")
print(f"Fastest response: {fastest_response} ms")
print(f"Slowest response: {slowest_response} ms")
print(f"Under 100 ms: {under_100}")
print(f"100–200 ms: {between_100_200}")
print(f"Above 200 ms: {above_200}")
print(f"Slow responses: {slow_responses}")
