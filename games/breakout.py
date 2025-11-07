import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.title("🧱 Breakout Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=6)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, -200)
ball.dx = 3
ball.dy = 3

# Bricks
bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]
for y in range(200, 100, -20):
    for x in range(-350, 350, 70):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(random.choice(colors))
        brick.shapesize(stretch_wid=1, stretch_len=3)
        brick.penup()
        brick.goto(x, y)
        bricks.append(brick)

# Score
score = 0
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.color("white")
score_display.penup()
score_display.goto(-380, 260)
score_display.write(f"Score: {score}", font=("Arial", 16, "normal"))

# Paddle movement
def move_left():
    x = paddle.xcor()
    if x > -350:
        paddle.setx(x - 40)

def move_right():
    x = paddle.xcor()
    if x < 350:
        paddle.setx(x + 40)

screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Game loop
while True:
    screen.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Wall collision
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.dx *= -1
    if ball.ycor() > 290:
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.goto(0, -200)
        ball.dy *= -1

    # Paddle collision
    if (ball.ycor() < -230 and ball.ycor() > -240) and abs(ball.xcor() - paddle.xcor()) < 60:
        ball.dy *= -1

    # Brick collision
    for brick in bricks:
        if ball.distance(brick) < 35:
            ball.dy *= -1
            brick.goto(1000, 1000)  # Hide brick
            bricks.remove(brick)
            score += 10
            score_display.clear()
            score_display.write(f"Score: {score}", font=("Arial", 16, "normal"))