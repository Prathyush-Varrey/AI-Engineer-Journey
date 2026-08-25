"""
9. 🔥 The Data Extraction Challenge

Imagine you receive this kind of structured text from an AI system:

USER:Prathyush|AGE:24|ROLE:AI Engineer|COUNTRY:India

Your program should extract and display:

Name: Prathyush
Age: 24
Role: AI Engineer
Country: India
Rules

You must use string slicing somewhere in your solution.

You can use the string methods you've learned, but don't use lists, loops, functions, or dictionaries yet.

Extra challenge

Now imagine the input changes:

USER:Rahul|AGE:27|ROLE:Data Scientist|COUNTRY:India

Your program should still work.

The goal here isn't merely extracting characters.

It's to make you think:

"How can I locate the information I need and then extract it?"

That's a very important transition from learning syntax to solving problems.
"""

structured_text = input("Enter your Text : ")

fist_collon_occurance = structured_text.find(":")
second_collon_occurance = structured_text.find(":", fist_collon_occurance + 1)
thrid_collon_occurance = structured_text.find(":",second_collon_occurance + 1)
last_collon_occurance = structured_text.rfind(":")

first_delimeter_occurance = structured_text.find("|")
second_delimeter_occurance = structured_text.find("|", first_delimeter_occurance + 1)
#thrid_delimeter_occurance = structured_text.find("|", second_collon_occurance + 1)
last_delimeter_occurance = structured_text.rfind("|")

user_name = structured_text[fist_collon_occurance + 1 : first_delimeter_occurance]
print(f"Name : {user_name}")

user_age = structured_text[second_collon_occurance + 1 : second_delimeter_occurance]
print(f"Age : {user_age}")

user_role = structured_text[thrid_collon_occurance + 1: last_delimeter_occurance]
print(f"Role : {user_role}")

user_country = structured_text[last_collon_occurance + 1 : ]
print(f"Country : {user_country}")