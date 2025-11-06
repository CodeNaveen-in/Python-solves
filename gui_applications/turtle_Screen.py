import turtle

timmy = turtle.Turtle()
print (timmy)
timmy.shape("turtle")
timmy.color("coral", "lightblue")  # stroke color, fill color
# timmy.forward(100) #meant to practice testing

my_screen = turtle.Screen()
print(my_screen.canvheight)

def make_square(turtle):
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)
make_square(timmy)

def dashed_line(turtle):
    for _ in range(15):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()
dashed_line(timmy)

my_screen.exitonclick()