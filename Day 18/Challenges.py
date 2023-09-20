'''
#------------- Draw a square -------------------
from turtle import Turtle, Screen
timmy = Turtle()
timmy.shape('turtle')
timmy.color('green')
for i in range(4):
    timmy.forward(100)
    timmy.left(90)

screen = Screen()
screen.exitonclick()


#------------- Draw a Dashed line -------------------
from turtle import Turtle, Screen
timmy = Turtle()
timmy.shape('turtle')
for i in range(10):
    # timmy.forward(10)
    # timmy.color('white')
    # timmy.forward(10)
    # timmy.color('black')

    timmy.forward(10)
    timmy.penup('white')
    timmy.forward(10)
    timmy.pendown('black')
screen = Screen()
screen.exitonclick()  '''
import random
from turtle import Turtle, Screen
import random
timmy = Turtle()
timmy.shape('turtle')
colors = ['light cyan','slate gray','dark sea green','dark khaki','lemon chiffon',
          'salmon','rosy brown','light coral','green yellow','cadet blue']
def shape(num_sides):
    angle = int(360//num_sides)
    for side in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

for side in range(3,11):
    timmy.color(random.choices(colors))
    shape(side)

screen = Screen()
screen.exitonclick()