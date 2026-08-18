name = "prathyush"

#length of the string
length = len(name)
print(length)

#find : find the index of the first occurrence of a substring in the string. If not found, it returns -1.
print(name.find("pr"))

# capitalize : returns a copy of the string with its first character capitalized and the rest lowercased.
print(name.capitalize())

#upper : returns a copy of the string with all the characters in uppercase.
print(name.upper())

#lower : returns a copy of the string with all the characters in lowercase.
print(name.lower())

#isdigit : returns True if all the characters in the string are digits, otherwise False.
print(name.isdigit())

#isalpha : returns True if all the characters in the string are alphabetic, otherwise False.
print(name.isalpha())

#count : returns the number of occurrences of a substring in the string.
print(name.count("h"))

#replace : returns a copy of the string with all occurrences of a substring replaced with another substring.
print(name.replace("pr", "ra"))

print(name * 10)

#strip : returns a copy of the string with leading and trailing whitespace removed.
name_with_spaces = "   prathyush   "
print(name_with_spaces.strip())

#split : returns a list of substrings in the string, split by a specified delimiter. If no delimiter is specified, it splits by whitespace.
print(name.split("a"))

#startswith : returns True if the string starts with a specified prefix, otherwise False.
print(name.startswith("pra"))

#endswith : returns True if the string ends with a specified suffix, otherwise False.
print(name.endswith("ush"))

#join : returns a string that is the concatenation of the strings in an iterable, separated by a specified delimiter.
words = ["hello", "world"]
print(" ".join(words))

#format : returns a copy of the string with placeholders replaced by specified values.
age = 25
print("My name is {} and I am {} years old.".format(name, age))