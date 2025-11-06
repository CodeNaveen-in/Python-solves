import turtle
import time
import random

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MOVE_DISTANCE = 20
DELAY = 0.1

# Snake class
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            self.add_segment((-MOVE_DISTANCE * i, 0))

    def add_segment(self, position):
        segment = turtle.Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].pos())
        self.head.forward(MOVE_DISTANCE)
        self.wrap_around()

    def wrap_around(self):
        x, y = self.head.xcor(), self.head.ycor()
        if x > SCREEN_WIDTH / 2:
            self.head.setx(-SCREEN_WIDTH / 2)
        elif x < -SCREEN_WIDTH / 2:
            self.head.setx(SCREEN_WIDTH / 2)
        if y > SCREEN_HEIGHT / 2:
            self.head.sety(-SCREEN_HEIGHT / 2)
        elif y < -SCREEN_HEIGHT / 2:
            self.head.sety(SCREEN_HEIGHT / 2)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

# Food class
class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.randint(-SCREEN_WIDTH//2 + 20, SCREEN_WIDTH//2 - 20)
        y = random.randint(-SCREEN_HEIGHT//2 + 20, SCREEN_HEIGHT//2 - 20)
        self.goto(x, y)

# Game setup
screen = turtle.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game 🐍")
screen.tracer(0)

snake = Snake()
food = Food()

# Game over writer
game_over_writer = turtle.Turtle()
game_over_writer.hideturtle()
game_over_writer.color("white")
game_over_writer.penup()

# Controls
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

# Game loop
game_on = True
while game_on:
    screen.update()
    time.sleep(DELAY)
    snake.move()

    # Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()

    # Collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            game_over_writer.goto(0, 0)
            game_over_writer.write("GAME OVER", align="center", font=("Arial", 24, "bold"))

screen.mainloop()