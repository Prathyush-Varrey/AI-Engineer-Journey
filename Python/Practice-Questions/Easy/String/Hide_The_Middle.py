"""
2. Hide the Middle

Ask the user for a word.

For example:

Enter word: PYTHON

Display:

P****N

The first and last characters should remain visible, while everything between them should be replaced with *.

Test with:

PYTHON
COMPUTER
AI

Think about what happens when the word has only two characters.
"""
user_input = input("Enter any Word :")

first_char_from_user_input = user_input[0]

last_char_from_user_input = user_input[-1]

middle_char_from_user_input = user_input[1:-1]
#print(middle_char_from_user_input)
masked_text = (first_char_from_user_input + "*" * len(middle_char_from_user_input) + last_char_from_user_input)

print(masked_text)


