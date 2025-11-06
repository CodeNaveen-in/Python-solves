import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.title("🐢 Turtle Race!")
screen.bgcolor("lightblue")
screen.setup(width=800, height=400)

# Draw finish line
finish_line = 350
line = turtle.Turtle()
line.hideturtle()
line.penup()
line.goto(finish_line, -150)
line.pendown()
line.left(90)
line.forward(300)

# Turtle colors and positions
colors = ["red", "blue", "green", "orange", "purple", "yellow"]
start_y = -100
turtles = []

# Create turtles
for color in colors:
    t = turtle.Turtle(shape="turtle")
    t.color(color)
    t.penup()
    t.goto(-350, start_y)
    start_y += 40
    turtles.append(t)

# Start race
winner = None
while not winner:
    for t in turtles:
        t.forward(random.randint(1, 10))
        if t.xcor() >= finish_line:
            winner = t
            break

# Announce winner
announce = turtle.Turtle()
announce.hideturtle()
announce.penup()
announce.goto(0, 150)
announce.write(f"{winner.color()[0].capitalize()} turtle wins!", align="center", font=("Arial", 24, "bold"))

screen.exitonclick()