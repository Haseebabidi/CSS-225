# Author: Haseeb Abidi
# Last Edited: 3/20/2025 
# Problem 6: Use a for statement to calculate the factorial of a user input value.
#  Print this value as well as the calculated value using the factorial function in the math module.



import math

# Ask the user to enter number
num = int(input("Enter a non-negative integer: "))


factorial = 1

# Use a for loop to calculate the factorial manually
for i in range(1, num + 1):
    factorial *= i  # Multiply each number from 1 to num

# Print the result from our loop
print("Factorial (calculated using loop):", factorial)


print("Factorial (using math.factorial):", math.factorial(num))
