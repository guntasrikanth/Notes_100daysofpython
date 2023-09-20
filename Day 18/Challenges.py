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
screen.exitonclick()

#------------- Draw a different angles -------------------
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

#------------- Random Walk-------------------

import turtle
import random
timmy = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)

def color_choice():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


direction =[0, 90, 180, 270]
timmy.pensize(10)
timmy.speed(8)

for _ in range(150):
    timmy.forward(20)
    timmy.setheading(random.choice(direction))
    timmy.color(color_choice())
    #screen.exitonclick()
'''

#------------- Spirograph -------------------

import turtle
import random
timmy = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)

def color_choice():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


timmy.speed(0)
def spirograph(angle):
    for _ in range(int(360 / angle)):
        timmy.color(color_choice())
        timmy.circle(100)
        #timmy.left(angle)
        timmy.setheading(timmy.heading() + angle)

spirograph(5)
screen.exitonclick()
