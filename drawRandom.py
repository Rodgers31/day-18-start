import random
from turtle import Turtle, Screen

t = Turtle()
colors = ["lawn green", "slate blue", "maroon", "indigo"]


def turning(move, forward):
    if move % 2 == 0:
        t.forward(forward)
        t.left(90)
    elif move % 2 < 30:
        t.left(180)
        t.forward(forward)
    elif move % 2 > 65:
        t.right(180)
        t.forward(forward)
    else:
        t.right(270)
        t.forward(forward)



for _ in range(100):
    turn = random.randint(1, 100)
    amount = random.randint(20, 60)
    for cx in colors:
        t.color(cx)
        t.pensize(10)
        t.speed(9)
        turning(turn, amount)


screen = Screen()
screen.exitonclick()
