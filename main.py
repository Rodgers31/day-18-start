import turtle
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")

# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

for _ in range(15):
    timmy_the_turtle.pen(pensize=1)
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()


# import heroes
#
# print(heroes.gen())




screen = Screen()
screen.setup(width=8000)
screen.exitonclick()