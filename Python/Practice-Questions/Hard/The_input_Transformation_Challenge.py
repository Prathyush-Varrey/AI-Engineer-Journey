"""
9. The Input Transformation Challenge

Build a program that asks the user to enter a sentence.

For example:

Enter sentence:   Python makes AI engineering FUN

Your program must produce:

Original: Python makes AI engineering FUN
Cleaned: Python makes AI engineering FUN
Uppercase: PYTHON MAKES AI ENGINEERING FUN
Lowercase: python makes ai engineering fun
Word count: 5

But here's the challenge:

The user could enter:

     Python    makes   AI engineering    FUN

Your program should still correctly determine that there are 5 words.

You're allowed to use only concepts you've learned so far:

Variables, multiple assignment, string methods, type casting, and user input.

Don't use loops, lists, functions, or anything you haven't learned yet.

"""

user_sentence = input("Enter sentence:").strip()

Cleaned_sentence = ' '.join(user_sentence.split())

Uppercase_sentence = Cleaned_sentence.upper()

lowercase_sentence = Cleaned_sentence.lower()

word_count = len(Cleaned_sentence.split())

print(f"Original: {user_sentence}")
print(f"Cleaned: {Cleaned_sentence}")
print(f"Uppercase: {Uppercase_sentence}")
print(f"Lowercase: {lowercase_sentence}")
print(f"Word count: {word_count}")

