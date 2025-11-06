import turtle
import random
import time

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_SPEED = 20
BALL_SPEED = 2

# Paddle class
class Paddle(turtle.Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_pos, 0)

    def move_up(self):
        if self.ycor() < 250:
            self.sety(self.ycor() + PADDLE_SPEED)

    def move_down(self):
        if self.ycor() > -240:
            self.sety(self.ycor() - PADDLE_SPEED)

# Ball class
class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.reset_position()

    def reset_position(self):
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        self.goto(x, y)
        self.dx = BALL_SPEED * random.choice([-1, 1])
        self.dy = BALL_SPEED * random.choice([-1, 1])

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1

# Scoreboard class
class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Player A: {self.score_left}  Player B: {self.score_right}", align="center", font=("Courier", 24, "normal"))

    def point_left(self):
        self.score_left += 1
        self.update_score()

    def point_right(self):
        self.score_right += 1
        self.update_score()

# Screen setup
screen = turtle.Screen()
screen.title("Pong Game 🏓")
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

# Create game objects
left_paddle = Paddle(-350)
right_paddle = Paddle(350)
ball = Ball()
scoreboard = Scoreboard()

# Key bindings
screen.listen()
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(screen.bye, "q")

# Game loop
while True:
    screen.update()
    time.sleep(0.01)
    ball.move()

    # Bounce off top and bottom
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Bounce off paddles
    if (340 < ball.xcor() < 350 and
        right_paddle.ycor() - 50 < ball.ycor() < right_paddle.ycor() + 50):
        ball.bounce_x()

    if (-350 < ball.xcor() < -340 and
        left_paddle.ycor() - 50 < ball.ycor() < left_paddle.ycor() + 50):
        ball.bounce_x()

    # Score update
    if ball.xcor() > 390:
        scoreboard.point_left()
        ball.reset_position()

    if ball.xcor() < -390:
        scoreboard.point_right()
        ball.reset_position()