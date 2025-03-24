# Haseeb
# Date: 3/25/25
# Problem 3: Multiply all numbers in a list

def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Example 
nums = [5, 2, 7, -1]
print("Product of the list is:", multiply_list(nums))
