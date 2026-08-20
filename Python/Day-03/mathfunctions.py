import math as math

pi = 3.14
deci_number = 14.50923
first_number = 10
second_number = 15
third_number = 5

# What does abs do in math? It returns the absolute value of a number. For example, abs(-5) would return 5.
#print(abs(pi))
#print(abs(first_number))
#print(abs(second_number))
#print(abs(third_number))   

#round() : It returns the nearest integer to a number.
"""
print(round(pi))
print(round(first_number))
print(round(second_number))
print(round(third_number))
"""

#min() : It returns the smallest value from a list of numbers.
#print(min(pi, first_number, second_number, third_number))

#max() : It returns the largest value from a list of numbers.
#print(max(pi, first_number, second_number, third_number))

#sum() : It returns the sum of all the numbers in a list.
numbers = [pi, first_number, second_number, third_number]
#print(sum(numbers))

#pow() : It returns the value of a number raised to the power of another number.
#print(math.pow(first_number, second_number))

# ** : It returns the value of a number raised to the power of another number.
#print(first_number ** second_number)

#// : It returns the floor division of a number by another number.
#print(first_number // second_number)

#% : It returns the remainder of a number divided by another number.
#print(first_number % second_number)

#divmod() : It returs a tuple containing their quotient and reminder
#print(divmod(first_number, second_number))

""" Now math fun using math module """
#math.sqrt() : returns square root of the given number
#print(math.sqrt(first_number))

#math.floor() :  rounds a number DOWN to the nearest integer, returning the largest integer less than or equal to x
#print(math.floor(deci_number))

#math.ceil() :  is used to round a number up to the nearest integer that is greater than or equal to that number.
#print(math.ceil(deci_number))

#math.log() :  calculates the natural logarithm (base e) of a number
#print(math.log(pi))

#math.exp() : In Python, math.exp(x) calculates \(e^{x}\), which is Euler's number 
# (\(e \approx 2.71828\)) raised to the power of \(x\)
#print(math.exp(first_number))

#math.log10() :  In Python, math.log10(x) calculates the base-10 logarithm of a number
#print(math.log10(third_number))


#math.log2() : math.log2(x) calculates the base-2 logarithm of a number,
#  which determines the power to which the number 2 must be raised to equal x.
#print(math.log2(second_number))

#math.isclose() : The Python math.isclose() function checks whether two floating-point numbers are
#  approximately equal within a specified tolerance. It returns True if the numbers are close enough, and False otherwise
print(math.isclose(first_number, deci_number, rel_tol=1e-09, abs_tol=0.0))