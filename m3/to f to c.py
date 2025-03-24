#author name Haseeb Abidi
#last Edited 2/16/2025
#this program just convert Fahrenheit to celsius.


F = int(input("write Fahrenheit: "))  # ask the user to input the fahrenhiet temprature.
C = 5 / 9 * (F - 32) # Convert Fahrenheit to Celsius using the formula: C = (5/9) * (F - 32)
print("Celsius is about ", round(C))  