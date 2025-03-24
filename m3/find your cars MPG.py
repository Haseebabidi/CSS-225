#author name Haseeb Abidi
#last Edited 2/15/2025
#this program help you see MPG of you car. with basic devide

miles = int(input("How many miles driven? "))#  to input the number of miles driven and convert it to an integer  
gallons = int(input("How many gallons used? "))  #  input the number of gallons used and convert it to an integer
MPG = int(miles / gallons)  # Calculate miles per gallon (MPG) by dividing miles by gallons

print("Your MPG is ", MPG)
