import turtle
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")

# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

for _ in range(50):
    turtle.position()
    turtle.pen(pensize=1)
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
    turtle.forward(10)

# import heroes
#
# print(heroes.gen())




screen = Screen()
screen.setup(width=8000)
screen.exitonclick()