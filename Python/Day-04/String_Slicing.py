#slicing = is a technique to extract specific portion or subset of elements from data sequence like string, list , tuples
# and array. indexing[] or slice() => indexing => [start:stop:step]

user_name = "Prathyush Varrey"

user_first_name = user_name[0:10]
print(user_first_name)

user_last_name = user_name[10:]
print()
print(user_last_name)

#using step will skip the charcter with th given number example if you enter 2 indexing skips 2 charcters and print the next charcter

daizy_user_name = user_name[::2]
print()
print(daizy_user_name)

#reverse string using indexing
reversed_user_name = user_name[::-1]
print()
print(reversed_user_name)

#slice
website = "https://google.com"

slice_obj = slice(8,-4)
print(website[slice_obj])