import random
import turtle
from turtle import Turtle, Screen

t = Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_color = (r, g, b)
    return my_color


directions = [0, 90, 180, 270]

for _ in range(200):
    t.pensize(15)
    t.speed('fastest')
    t.color(random_color())
    t.forward(30)
    t.setheading((random.choice(directions)))

# def turning(move, forward):
#     if move % 2 == 0:
#         t.forward(forward)
#         t.left(90)
#     elif move % 2 < 30:
#         t.left(180)
#         t.forward(forward)
#     elif move % 2 > 65:
#         t.right(180)
#         t.forward(forward)
#     else:
#         t.right(270)
#         t.forward(forward)
#
#
# for _ in range(100):
#     turn = random.randint(1, 100)
#     amount = random.randint(20, 60)
#     for cx in colors:
#         t.color(cx)
#         t.pensize(10)
#         t.speed(9)
#         turning(turn, amount)


screen = Screen()
screen.exitonclick()
