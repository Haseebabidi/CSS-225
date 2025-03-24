# Author: Haseeb Abidi    
# Last Edited: 3/20/2025 
# Problem 4:  Search on the internet for a way to calculate an approximation for pi. 
# There are many that use simple arithmetic. Write a program to compute the approximation 
# and then print that value as well as the value of math.pi from the math module. 



import math

# We'll use this many terms to get a decent approximation of pi
num_terms = 100000
approximation = 0.0

# Using the Leibniz formula to estimate pi
# Basically: pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - etx
for p in range(num_terms):
    approximation += (-1)**p / (2 * p + 1)

# Multiply by 4 because the formula gives us pi/4
approximation *= 4

# Print both the estimated value and the actual value from Python's math module
print("Approximated pi:", approximation)
print("math.pi:", math.pi)