import turtle

timmy = turtle.Turtle()
print (timmy)
timmy.shape("turtle")
timmy.color("coral", "lightblue")  # stroke color, fill color
timmy.forward(100)

my_screen = turtle.Screen()
print(my_screen.canvheight)

my_screen.exitonclick()