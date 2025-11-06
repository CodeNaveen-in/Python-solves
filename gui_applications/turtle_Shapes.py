from turtle import Turtle

def make_triangle(turtle):
    for _ in range(3):
        turtle.forward(100)
        turtle.right(120)

def make_square(turtle):
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

def make_pentagon(turtle):
    for _ in range(5):
        turtle.forward(100)
        turtle.right(72)

def make_hexagon(turtle):
    for _ in range(6):
        turtle.forward(100)
        turtle.right(60)

def make_heptagon(turtle):
    for _ in range(7):
        turtle.forward(100)
        turtle.right(51.43)

def make_octagon(turtle):
    for _ in range(8):
        turtle.forward(100)
        turtle.right(45)

def make_nonagon(turtle):
    for _ in range(9):
        turtle.forward(100)
        turtle.right(40)

def make_decagon(turtle):
    for _ in range(10):
        turtle.forward(100)
        turtle.right(36)

timmy = Turtle()

make_triangle(timmy)
make_square(timmy)
make_pentagon(timmy)
make_hexagon(timmy)
make_heptagon(timmy)
make_octagon(timmy)
make_nonagon(timmy)
make_decagon(timmy)