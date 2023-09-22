from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def fd():
    tim.forward(10)

# event listener
screen.listen()

#passing a function(fd) as a parameter to another method(onkey)
screen.onkey(fun=fd, key="Down")
screen.exitonclick()