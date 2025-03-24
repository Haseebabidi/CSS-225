# Haseeb
# Date: 3/23/25
# Problem 4: Determine if a year is a leap year

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            return True
    return False

# Example usage
print("Leap year check:", is_leap_year(2024))
