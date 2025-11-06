from turtle import Turtle, Screen

t = Turtle()
s = Screen()

s.title("Etch A Sketch")
s.bgcolor("black")
s.setup(width=600, height=600)

t.pensize(5)
t.color("white")
t.speed(0)

def move_forward():
    t.setheading(90)
    t.forward(10)

def move_backward():
    t.setheading(270)
    t.forward(10)

def move_left():
    t.setheading(180)
    t.forward(10)

def move_right():
    t.setheading(0)
    t.forward(10)

def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

s.listen()
s.onkey(fun=move_forward, key="w")
s.onkey(fun=move_backward, key="s")
s.onkey(fun=move_left, key="a")
s.onkey(fun=move_right,key="d")
s.onkey(clear_screen, "c")
s.onkey(s.bye, "q")

s.mainloop()