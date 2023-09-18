from turtle import Turtle, Screen
from prettytable import PrettyTable

''''jimmy = Turtle()
jimmy.shape("turtle")
jimmy.color("red")
for steps in range(100):
    for c in ('blue', 'red', 'green'):
        jimmy.color(c)
        jimmy.forward(steps)
        jimmy.right(30)

my_screen = Screen()
my_screen.exitonclick() '''

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = 'l'              
print(table)