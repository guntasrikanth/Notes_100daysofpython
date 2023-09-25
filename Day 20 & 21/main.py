import time
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in positions:
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(position)
    segments.append(segment)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.3)
    for seg in segments:
        seg.forward(10)





















screen.exitonclick()