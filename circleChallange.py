import turtle
from turtle import Turtle, Screen
import random

t = Turtle()
turtle.colormode(255)
turtle.position()


def my_color():
    r = random.randint(0, 205)
    g = random.randint(0, 205)
    b = random.randint(0, 205)
    colors = (r, g, b)
    return colors


circle = True

while circle:
    t.color(my_color())
    t.speed(15)
    t.tilt(90)
    t.circle(100)
    t.left(15)
    t.circle(50)
    if t.heading() == 0.0:
        circle = False

screen = Screen()
screen.exitonclick()
