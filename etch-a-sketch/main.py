from turtle import Turtle, Screen
import random

screen = Screen()
is_on = False
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make your bet", prompt="Who will win? Choose your color: ")

colors = ["pink", "blue", "green", "yellow", "orange", "red"]

n = -100
i = 0
turtles = []
for turtle in range(0, 6):

    tim = Turtle(shape="turtle")
    tim.penup()
    tim.goto(x=-230, y=n)
    tim.color(colors[i])
    turtles.append(tim)
    n += 30
    i += 1
if user_input:
    is_on = True

while is_on:

    for turtle in turtles:
        dist = random.randint(0, 10)
        if turtle.xcor() > 230:
            is_on = False
            win_color = turtle.pencolor()
            if win_color == user_input:
                print(f"You won. {win_color} turtle is winner")
            else:
                print(f"You lost. {win_color} won ")

        turtle.forward(dist)


screen.exitonclick()
