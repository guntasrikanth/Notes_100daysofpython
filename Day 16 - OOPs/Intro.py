from turtle import Turtle, Screen

jimmy = Turtle()
jimmy.shape("turtle")
jimmy.color("red")
for steps in range(100):
    for c in ('blue', 'red', 'green'):
        jimmy.color(c)
        jimmy.forward(steps)
        jimmy.right(30)



my_screen = Screen()
my_screen.exitonclick()
