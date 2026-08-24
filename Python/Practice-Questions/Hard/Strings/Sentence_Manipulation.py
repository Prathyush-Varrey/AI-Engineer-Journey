"""
8. Sentence Manipulation Challenge

Ask the user to enter:

Python makes artificial intelligence interesting

Your program should produce:

First 6 characters: Python
Last 9 characters: interesting
Reversed: gnitseretni ecnegilletni laicifitra sekam nohtyP

But there's a catch:

You cannot hard-code the positions of the first and last words.

Your program needs to determine the relevant positions from the user's input.

Think about how the concepts you've learned so far can work together:

String methods
      ↓
Find useful information
      ↓
String slicing
      ↓
Output
"""
user_input = input("Enter a Snetence :").strip()
first_six_chars = user_input[0:6]
print(f"First 6 characters: {first_six_chars}")

find_last_space_occurance = user_input.rfind(" ")
#print(find_last_space_occurance)
last_nine_chars = user_input[find_last_space_occurance + 1:]
print(f"Last 9 characters: {last_nine_chars}")

reversed_string = user_input[::-1]
print(f"Reversed: {reversed_string}")