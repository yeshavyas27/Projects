from turtle import Turtle, Screen, colormode
import random

colors_list = [(132, 166, 204), (220, 148, 108), (197, 135, 148), (32, 41, 61), (163, 59, 49), (41, 106, 155),
               (141, 183, 162), (237, 211, 92), (148, 61, 68), (214, 83, 72), (35, 61, 56), (52, 111, 91),
               (170, 29, 33), (158, 33, 30), (234, 167, 158), (17, 97, 71), (52, 44, 48), (230, 161, 165),
               (171, 188, 220), (58, 52, 49), (184, 103, 113), (32, 60, 108), (107, 127, 159), (175, 200, 188),
               (35, 150, 209), (66, 66, 56)]

colormode(255)
tim = Turtle()
screen = Screen()

tim.setx(0)
tim.sety(-250)
pos = 50

for _ in range(0, 10):
    tim.clearstamp(1)

    for _ in range(0, 10):
        color = random.choice(colors_list)
        tim.dot(20, color)
        tim.penup()
        tim.forward(50)

    tim.goto(0, pos)
    pos += 50

screen.exitonclick()












