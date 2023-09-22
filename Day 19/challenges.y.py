from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
def forward():
    tim.forward(10)

def backward():
    tim.backward(10)

def clock_rotation():
    tim.left(10)

def anti_clock_rotation():
    tim.right(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


tim.speed('slow')
screen.listen()
screen.onkey(fun=forward, key="W")
screen.onkey(fun=backward, key="S")
screen.onkey(fun=clock_rotation, key="A")
screen.onkey(fun=anti_clock_rotation, key="D")
screen.onkey(fun=clear, key="C")

screen.exitonclick()
