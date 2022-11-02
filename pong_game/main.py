from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
screen = Screen()
ball = Ball()
scoreboard = Scoreboard()



screen.bgcolor("black")
screen.setup(800, 600)
screen.title("pong")
screen.tracer(0)
screen.listen()


screen.onkey(l_paddle.up, key="w")
screen.onkey(l_paddle.down, key="s")
screen.onkey(r_paddle.up, key="Up")
screen.onkey(r_paddle.down, key="Down")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    # detect ball hits top or bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detect if ball hits the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
    # detect if ball missed by the r_paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    # detect if ball missed by the l_paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
    screen.update()


screen.exitonclick()
