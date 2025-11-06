from turtle import Turtle, Screen, colormode
import random

colormode(255)  # Enable RGB mode

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def move_turtle():
    angle = random.choice([0, 90, 180, 270])
    distance = random.randint(20, 100)
    t.pensize(5)
    t.setheading(angle)
    t.forward(distance)

t = Turtle()
s = Screen()
s.title("Random Walk Turtle")

for _ in range(random.randint(10, 200)):
    t.pencolor(random_color())
    move_turtle()

s.exitonclick()