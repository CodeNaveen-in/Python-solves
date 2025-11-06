from turtle import Turtle, Screen, colormode
import random

colormode(255)  # Enable RGB mode

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)
        t.speed("fastest")

t = Turtle()
s = Screen()
s.title("Spirograph")

draw_spirograph(5)

s.exitonclick()