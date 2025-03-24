#author name Haseeb Abidi
#last Edited 2/19/2025
#Problem 4 – Consider a program that iterates the integers from 1 to 50. For multiples of three
# print “Divisible by three” instead of the number and for the multiples of five print “Divisible by
# five”. For numbers which are multiples of both three and five print “Divisible by both”. Use
# draw.io to draw the flow of execution. Then write the program. Submit both the flowchart and
# the code.

#this program help you find number in range from 1,50 divisablity from 5,3 or both


for number in range(1, 51):  # Loop through numbers from 1 to 50
    
    if number % 3 == 0 and number % 5 == 0:  # Check if the number is divide by 3 and 5.
        print("Divisible by both")  
    
    elif number % 3 == 0:  # Check if the number is divisible by 3 only
        print("Divisible by three")  
    
    # Check if the number is divisible by 5 only
    elif number % 5 == 0:  
        print("Divisible by five")  # Print message for numbers like 5, 10, 20, 25
    
    # If the number is not divisible by 3 or 5, print the number itself
    else:  
        print(number)  # Print the actual number (e.g., 1, 2, 4, 7, 8, etc.)