import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(fun=player.move_forward, key="Up")

scoreboard = Scoreboard()
cars = []
for _ in range(0, 20):
    temp_car = CarManager()
    cars.append(temp_car)

player.move_to_start()
screen.update()
game_is_on = True
while game_is_on:
    time.sleep(0.1)

    for car in cars:
        if car.xcor() < -280:
            new_y = random.randint(-275, 275)
            car.goto(y=new_y, x=-car.xcor())
        if player.distance(car) < 20:
            screen.clear()
            scoreboard.game_over()
            game_is_on = False
        if scoreboard.level == 1:
            car.move_forward_level1()
        elif scoreboard.level == 2:
            car.move_forward_level2()

    if player.ycor() > 280 and scoreboard.level == 1:
        player.goto(0, -280)
        scoreboard.level = 2
        scoreboard.level_write()

    elif player.ycor() > 280 and scoreboard.level == 2:
        screen.clear()
        scoreboard.you_win()

    screen.update()

screen.exitonclick()
