"""
5. Text Analyzer

Ask the user to enter a sentence.

Your program should display:

Original sentence: Python is Amazing
Characters: 18
Uppercase: PYTHON IS AMAZING
Lowercase: python is amazing

Important: Don't manually count the characters.

Also think about whether spaces should be included in your character count and make a deliberate choice.

Approch :
                Ask the user to enter a sentence
                         |
                Count the number of characters in the sentence
                         |
                convert the sentence to upper and lower case
                        |
                Diesplay the output in the required format            
"""

user_sentence = input("Enter a sentence:").strip()

number_of_characters = len(user_sentence)
uppercase_sentence = user_sentence.upper()
lowercase_sentence = user_sentence.lower()

print(f"Original sentence : {user_sentence}")
print(f"Characters : {number_of_characters}")
print(f"Uppercase : {uppercase_sentence}")
print(f"Lowercase : {lowercase_sentence}")