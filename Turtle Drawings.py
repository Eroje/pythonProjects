# Let's draw some cool drawings with the package turtle

# Import turtle
import turtle

# Let's get a nice setup in turtle
turtle.bgcolor("black") # Background colour
turtle.pensize(2) # pen size
turtle.color("red")
turtle.speed(0)

# Draw a square
# turtle.forward(50)  # Moves forward
# turtle.left(90)  # Moves left 90 degrees
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.done()  # Allows turtle to stay on the screen

# Nice little project in turtle - creates a nice graph

# for colours in ["red", "orange", "yellow", "green", "blue", "purple"]:
#     turtle.color(colours)
#     turtle.circle(150)
#     turtle.left(60)

# Lets make it cooler
for i in range(12):
    for colours in ["red", "orange", "yellow", "green", "blue", "purple"]:
        turtle.color(colours)
        turtle.circle(150)
        turtle.left(5)
turtle.done()


