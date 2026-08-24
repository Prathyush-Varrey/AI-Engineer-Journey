"""
5. AI API Key Masker

Imagine you're displaying an API key in a log and don't want to expose the entire key.

Input:

Enter API key: sk-1234567890abcdef

Output:

Masked key: sk-************cdef

Keep:

the first 3 characters
the last 4 characters

Replace everything in between with *.

Your program should work with different API-key lengths.

Think carefully: You're not just extracting a substring—you need to combine multiple slices with another string.
"""

user_api_key = input("Enter Your API key : ")
first_three_chars_apikey = user_api_key[0:3]
#print(first_three_chars_apikey)
last_four_chars_apikey = user_api_key[-4:]
#print(last_four_chars_apikey)
middle_string_apikey = user_api_key[3:-4]
#print(middle_string_apikey)
masked_key = (first_three_chars_apikey + "*" * len(middle_string_apikey) + last_four_chars_apikey)
print(f"Masked Key : {masked_key}")