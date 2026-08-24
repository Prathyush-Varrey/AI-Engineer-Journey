"""
7. Build a Simple Text Preview

Imagine you're building a document-processing system.

Ask the user for a long piece of text.

Your program should:

Remove leading/trailing spaces.
If the text is longer than 50 characters, display only the first 50 characters followed by ....
If it's 50 characters or shorter, display the complete text.
Display the number of characters in the original cleaned text.

Example:

Enter text: Python is one of the most popular programming languages used for artificial intelligence and machine learning.


Characters: 109
Preview: Python is one of the most popular programming languages...

Important: Don't manually count characters.

Think about how you can combine:

string method + length + slicing + conditional logic

You haven't formally learned if yet in this session, but you already encountered it in the course. If you haven't practiced it yet, solve the slicing portion first and tell me where you got stuck.
"""

user_paragraph = input("Enter a long paragraph :").strip()

length_user_paragraph = len(user_paragraph)
#print(length_user_paragraph)
#text = user_paragraph[0 : length_user_paragraph]
#print(preview_text)

print(f"Characters : {length_user_paragraph}")

first_fifty_chars = user_paragraph[0 : 50]
if(length_user_paragraph > 50):
    preview_text = (first_fifty_chars + "...")
    print(f"Preview : {preview_text}")
else:
    print(f"Preview : {user_paragraph}")