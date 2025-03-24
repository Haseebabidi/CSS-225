# Author: Haseeb Abidi    
# Last Edited: 3/20/2025 import math
# Problem 5: Search the internet for how to convert radians to degrees. Write a program to compute the conversion given a user input value.
#  Print this value as well as the calculated value using the degrees function in the math module.


import math

# Ask the user to enter an angle in radians
radians = float(input("Enter an angle in radians: "))

# Manually convert radians to degrees using the formula: "degrees = radians * (180 / pi)"
manual_conversion = radians * (180 / math.pi)

# Use the built in function from the math module for comparison
builtin_conversion = math.degrees(radians)

# Print both values
print("Converted using formula:", manual_conversion)
print("Converted using math.degrees():", builtin_conversion)
