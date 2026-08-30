# list = in python used to store multiple items in a single variable

fav_food = ["Chicken", "Motton", "Biryani", "Ice-cream"]

#print(fav_food)

nums = list((1,2,3,4,5))
#print(nums)

name = list("bhanu")
#print(name)

# accessing elements
#print("Accessing Elements")
#print(fav_food[0])
#print(fav_food[-1])


# Adding Elements

#1. append(): Adds an element at the end of the list.
fav_food.append("chocolate")
#print(fav_food)


#2. insert(): Adds an element at a specific position.
fav_food.insert(2, "chapati")
#print(fav_food)

#3. extend(): Adds multiple elements to the end of the list.
#fav_food.extend([2,3])
#print(fav_food)

#Updating Elements
#Since lists are mutable, elements can be updated by assigning new values using their index.
fav_food[1] = "panner"
#print(fav_food)

# Removing Elements
#1. remove(): Removes the first occurrence of an element.
a = [1,2,3,4,5]

#a.remove(2)
#print(a)

#2. pop(): Removes the element at a specific index or the last element if no index is specified.
#a.pop()
#print(a)

#3. del statement: Deletes an element at a specified index.
#del a[1]
#print(a)

#4. clear(): removes all items.
a.clear()
#print(a)

#Iterating Over Lists
for item in fav_food:
    print(item)

#enumerate
for index, item in enumerate(fav_food):
    print(index, item)