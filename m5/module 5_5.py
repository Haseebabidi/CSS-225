#author name Haseeb Abidi
#last Edited 2/22/2025
#this command i try to make a NLU sign took me a quiet a wile to do that. but because of it i learn goto command
#and penup and pendown.

import turtle

screen = turtle.Screen()
screen.bgcolor("blue")  # background color 

# Set up the turtle for drawing
t = turtle.Turtle()

t.penup()

# Draw the thick border using forward and left
def draw_border():
    t.pensize(20)  #to thick the border thickness
    t.color("white")  # Set border color to white
    t.goto(-200, 100)  #  position 
    t.pendown()


    t.penup()

# Draw the white triangle in the center
def draw_triangle():
    t.goto(-180, -20)  # Positioning to start the triangle trying to make in the center professor
    t.setheading(0)  
    t.pendown()
    t.color("white")  # Set triangle color to white

   
    for _ in range(3): #this loop for making trangle
        t.forward(300)  # Move forward for each side of the triangle
        t.left(120)  # Turn left 120 degrees to form the triangle corners

    t.penup()


def write_text():
    t.goto(-90, 30)  # Position the text inside the triangle to make the logo
    t.color("white")  
    t.pendown()
    t.write("NLU", font=("Arial", 48, "bold"))  # Write "NLU" text
    t.penup()


draw_border()
draw_triangle()
write_text()


turtle.done()