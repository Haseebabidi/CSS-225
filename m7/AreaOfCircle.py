# Haseeb
# Date: 3/21/25
# Problem 1: Write a function areaOfCircle(r) which returns the area of a circle of radius r.
# This function uses the math module.

import math

def areaOfCircle(r):
    return math.pi * r * r

# Example 
radius = float(input("Enter the radius of the circle: "))
print("Area of the circle is:", areaOfCircle(radius))
