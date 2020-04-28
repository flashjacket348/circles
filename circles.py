##
# circle.py
# Calculate circumference and area of a circle
# v0.2

import math

radius = int(input(" Enter radius: " ))

print("Circumference: " , 2 * radius * math.pi)

print("Area: " , math.pi * radius ** 2)
