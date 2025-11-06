import colorgram
import turtle as t
import random

colors = colorgram.extract('sweet_pic.jpg', 6)
color_list = []
for color in colors:
    rgb = color.rgb
    color_list.append((rgb.r, rgb.g, rgb.b))
print(color_list)

def hirst_painting(dot_size, dot_num, dot_gap):

    t.colormode(255)
    tim = t.Turtle()
    tim.speed("fastest")
    tim.penup()
    tim.hideturtle()
    tim.setheading(225)
    tim.forward(250)
    tim.setheading(0)

    for dot_count in range(dot_num):
        tim.dot(dot_size, random.choice(color_list))
        tim.forward(dot_gap)

        if (dot_count + 1) % int(dot_num ** 0.5) == 0:
            tim.setheading(90)
            tim.forward(dot_gap)
            tim.setheading(180)
            tim.forward(dot_gap * int(dot_num ** 0.5))
            tim.setheading(0)

    screen = t.Screen()
    screen.exitonclick()
    
hirst_painting(20, 100, 50)