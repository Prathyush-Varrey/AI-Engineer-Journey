"""
5. AI Text Analyzer

Imagine you're processing a piece of text before sending it to an AI model.

Ask the user for a sentence.

Your program should calculate:

Total characters
Number of vowels
Number of consonants
Number of digits
Number of spaces

Example:

Enter text: AI Engineer 2026

Characters: 16
Vowels: 5
Consonants: 6
Digits: 4
Spaces: 2

You need to inspect the text character by character.

Challenge: Don't manually count anything.

Think about how for + if + logical operators can work together.
"""

sentence = input("Enter A Sentence : ")

Total_Chars = len(sentence)
#print(Total_Chars)
#vowels
#has_vowel = False
vowel_count = 0
vowels = "aeiouAEIOU"
#consonants
#has_consonants = False
consonant_count = 0
#consonant = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

# digits
digit_count = 0

# spaces
space_count = 0

#looping thourgh sentence
for char in sentence:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char == " ":
        space_count += 1


print(f"Characters: {Total_Chars}")

print(f"Vowels: {vowel_count}")

print(f"Consonants: {consonant_count}")

print(f"Digits: {digit_count}")

print(f"Spaces: {space_count}")