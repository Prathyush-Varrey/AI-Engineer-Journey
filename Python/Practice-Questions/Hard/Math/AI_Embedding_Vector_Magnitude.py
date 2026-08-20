"""
7. AI Embedding Vector Magnitude
Imagine an AI model produces a very small vector:
[3, 4]
The magnitude of a 2D vector is:
√(x² + y²)
Ask the user for x and y, then calculate the vector magnitude.
Example:
x: 3
y: 4

Vector magnitude: 5
Now test it with:
x: 6
y: 8
and:
x: -3
y: -4
Don't hard-code the answer.
Reasoning challenge: Think about how negative values affect the calculation.
"""
import math as math

x = int(input("Enter X Value :"))
y = int(input("Enter Y Value :"))
vector_magnitude = (math.sqrt(pow(x,2) + pow(y,2)))
print(vector_magnitude)