# Haseeb
# Date: 3/22/25
# Problem 2: Function to check whether a number is in range(1,10)

def check_range(num):
    if num in range(1, 10):
        print(f"{num} is in the range.")
    else:
        print(f"{num} is not in the range.")

# Example 
number = int(input("Enter a number: "))
check_range(number)
