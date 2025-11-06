import turtle
import time
import random

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1.1  # 10% speed increase

# Player class
class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.goto(0, -SCREEN_HEIGHT//2 + 20)
        self.setheading(90)

    def move_up(self):
        self.forward(20)

    def reset_position(self):
        self.goto(0, -SCREEN_HEIGHT//2 + 20)

# Car class
class Car(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(["red", "blue", "green", "yellow", "orange", "purple"]))
        self.penup()
        self.setheading(180)  # Move left
        self.goto(SCREEN_WIDTH / 2, random.randint(-250, 250))  # Start from right edge

    def move(self, speed):
        self.forward(speed)

# CarManager class
class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.random() < 0.1:
            new_car = Car()
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.move(self.speed)

    def increase_speed(self):
        self.speed *= MOVE_INCREMENT

# Scoreboard class
class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-SCREEN_WIDTH//2 + 20, SCREEN_HEIGHT//2 - 40)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=("Courier", 18, "bold"))

    def level_up(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "bold"))

# Screen setup
screen = turtle.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Turtle Crossing Game 🐢")
screen.tracer(0)

# Game objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Controls
screen.listen()
screen.onkeypress(player.move_up, "w")

# Game loop
game_on = True
while game_on:
    time.sleep(0.05)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Collision detection
    for car in car_manager.cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_on = False

    # Successful crossing
    if player.ycor() > SCREEN_HEIGHT//2 - 20:
        player.reset_position()
        car_manager.increase_speed()
        scoreboard.level_up()

screen.mainloop()