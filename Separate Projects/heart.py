import turtle
import time


# Function to draw a heart
def draw_heart():
    turtle.up()
    turtle.goto(0, -100)
    turtle.down()
    turtle.begin_fill()
    turtle.color('magenta')
    turtle.left(140)
    turtle.forward(224)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.left(120)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.forward(224)
    turtle.end_fill()


# Set up the turtle
turtle.setup(width=600, height=600)
turtle.speed(2)

# Set the background color
turtle.bgcolor('black')

# Draw the heart
draw_heart()

# Display the heart for 10 seconds
time.sleep(10)

# Close the turtle window
turtle.bye()
