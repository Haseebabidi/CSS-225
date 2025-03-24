# Haseeb
# Date:3/20/25
# Problem 5: Drawing squares using turtle (assuming visual representation)

import turtle

# Set up the window
window = turtle.Screen()
window.bgcolor("white")

# Create turtle
my_turtle = turtle.Turtle()

# Draw multiple squares
for i in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)

# Prevent the window from closing immediately
turtle.done()
