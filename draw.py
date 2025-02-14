import math
import random
from turtle import Turtle, Screen


t = Turtle()
shapes = {"triangle": 3, "square": 4, "pentagon": 5, "hexagon": 6,
         "heptagon": 7, "octago": 8, "nanogon": 9, "decagon": 10}


def movers(amount, turn):
    for _ in range(amount):
        rand_color = random.choices(range(255), k=3)
        # print('test', rand_color[0])
        # t.pencolor(int(rand_color[0]), int(rand_color[1]), int(rand_color[2]))
        t.color(int(rand_color[0]), int(rand_color[1]), int(rand_color[2]))
        t.forward(100)
        t.right(turn)


for shape in shapes:
    rotate = math.floor(360 / shapes[shape])
    print(shapes[shape])
    print(rotate)
    movers(int(shapes[shape]), rotate)




