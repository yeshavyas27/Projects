from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.level_write()

    def level_write(self):
        self.clear()
        self.goto(-280, 260)
        self.write(arg=f"Level {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)

    def you_win(self):
        self.goto(0, 0)
        self.write(arg="YOU WIN", align="center", font=FONT)
