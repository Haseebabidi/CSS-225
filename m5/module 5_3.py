#author name Haseeb Abidi
#last Edited 2/14/2025
#Problem 3 – Write a program that asks the user for the number of sides, the length of the side,
#the color of the line, and the fill color of a regular polygon. The program should draw the
#polygon and then fill it in.

#this program help you make polygons shapes and costumize it.


import turtle  # Importing the turtle module

# Taking user inputs
sides = int(input("Input your number of sides: "))
length = int(input("Input the length of each side: "))
line_color = input("Input your pen color: ")
fill_color = input("Input your fill color: ")

# Setting up the turtle
turtle.color(line_color)  # make the outline color.
turtle.begin_fill()
turtle.fillcolor(fill_color)  # set the fill color.

# Drawing the polygon
for _ in range(sides):
    turtle.forward(length)  # Move forward by the specified length.
    turtle.left(360 / sides)  # Turn left by the correct angle this will help us make correct shapes.

turtle.end_fill()  # Fill the shape
turtle.done()  # Keep the turtle window open