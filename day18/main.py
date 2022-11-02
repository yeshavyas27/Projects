from turtle import Turtle, Screen
import random


tim = Turtle()
screen = Screen()
# tim.shape("turtle")
tim.color("steel blue")
tim.speed("fastest")


def change_color():
    r = random.random()
    g = random.random()
    b = random.random()
    random_color = (r, g, b)

    return random_color


angle = 10

for _ in range(0, 36):
    tim.circle(100)
    tim.setheading(angle)
    tim.color(change_color())
    angle += 10

screen.exitonclick()
