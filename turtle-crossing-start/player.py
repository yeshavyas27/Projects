from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
FACE_FORWARD_ANGLE = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()

    def move_to_start(self):
        self.goto(STARTING_POSITION)
        self.left(FACE_FORWARD_ANGLE)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)