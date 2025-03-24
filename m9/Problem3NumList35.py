# Haseeb Abidi
# Date: 3/23/25
# Problem 3: Ask the user for numbers until their sum is greater than 100

numbers = []
total = 0

while total <= 100:
    num = float(input("Enter a number: "))
    numbers.append(num)
    total += num

print("Numbers entered:", numbers)
print("Sum of numbers:", total)
