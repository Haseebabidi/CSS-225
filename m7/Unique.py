# Haseeb
# Date: 3/20/25
# Problem 4: Return a new list with unique elements

def unique_elements(numbers):
    unique = []
    for num in numbers:
        if num not in unique:
            unique.append(num)
    return unique

# Example usage
original_list = [1, 3, 3, 3, 6, 2, 3, 5]
print("Unique elements:", unique_elements(original_list))
