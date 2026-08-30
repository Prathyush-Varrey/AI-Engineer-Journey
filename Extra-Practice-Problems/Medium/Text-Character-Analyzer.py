"""
4. Text Character Analyzer

Ask the user for a sentence.

Example:

Enter text: Python AI 2026

Analyze every character and display:

Letters: 8
Digits: 4
Spaces: 2
Special characters: 0

Then display:

Uppercase letters: 4
Lowercase letters: 4
Rules

You need to inspect the string one character at a time.

Don't manually count.

Think

What categories can each character belong to?

A character shouldn't accidentally be counted twice when it belongs to mutually exclusive categories.
"""

text = input("Enter Text: ").strip()
letters = 0
digits = 0
spaces = 0
special_char = 0
upper_case = 0
lower_case =0
for i in text:
    if i.isalpha():
        letters += 1
        if i == i.upper():
            upper_case += 1
        else:
            lower_case += 1
    elif i.isdigit():
        digits += 1
    elif i == " ":
        spaces += 1
    else:
        special_char += 1

print(f"Letters: {letters}")

print(f"Digits: {digits}")

print(f"Spaces: {spaces}")

print(f"Special characters: {special_char}")

print(f"Uppercase letters: {upper_case}")

print(f"Lowercase letters: {lower_case}")