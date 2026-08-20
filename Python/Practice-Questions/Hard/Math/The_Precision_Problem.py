"""
8. The Precision Problem

A program receives a measurement:

measurement = 17.856294

You need to display three different versions:

Original: 17.856294
Rounded: 17.86
Floor: 17
Ceiling: 18

Ask the user for the measurement rather than hard-coding it.

Then produce all three values.

Important: Understand the conceptual difference between:

rounding
flooring
ceiling

Don't simply try functions until the output looks right.
"""
import math as math

measurement = float(input("Enter The Measurment :"))
rounded_measurement = round(measurement,2)
floor_measurement = math.floor(measurement)
ceiling_measurement = math.ceil(measurement)

print(f"Original: {measurement}")
print(f"Rounded: {rounded_measurement}")
print(f"Floor: {floor_measurement}")
print(f"Ceiling: {ceiling_measurement}")