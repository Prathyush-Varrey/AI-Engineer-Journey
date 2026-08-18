#what is type casting in python
#Type casting in Python refers to the process of converting a variable from one data type to another.

x = 1 #int
y = 2.0 #float
z = "3" #string

print(x, type(x))
print(y, type(y))
print(z, type(z))

#Type Casting 
a = float(x) #int to float
b = int(y) #float to int
c = str(x) #int to string
d = int(z) #string to int

print("-----------------------------")

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))