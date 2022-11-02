from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=2)
        self.color(random.choice(COLORS))
        self.goto_random_position()

    def goto_random_position(self):

        x = random.randint(-275, 275)
        y = random.randint(-275, 275)
        self.goto(x, y)

    def move_forward_level1(self):
        self.backward(STARTING_MOVE_DISTANCE)

    def move_forward_level2(self):
        self.backward(MOVE_INCREMENT)



