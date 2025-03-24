# Haseeb
# Date: 3/23/25
# Problem 2: Check if sum of two numbers is >, <, or = 10

def compare_sum():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    total = a + b
    if total > 10:
        print("The sum is greater than 10.")
    elif total < 10:
        print("The sum is less than 10.")
    else:
        print("The sum is exactly 10.")

compare_sum()
