'''
--------------Ways of import modules-----------------------
####### First method ###########

#importing the module
import turtle
#access the classes from the module by adding module. from it
tim = turtle.Turtle

###### Second Method ###########

#by using this we can import classes directly
from turtle import Turtle, Screen
timmy = Turtle()
timmy.shape('turtle')

screen = Screen()
screen.exitonclick()

###### Third Method ###########
#By using this we can import everything from the turtle module
from turtle import *
timmy = Turtle()
timmy.shape('turtle')

screen = Screen()
screen.exitonclick()
--------------Ways of import modules-----------------------
'''

