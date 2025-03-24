from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)

game_is_on = True

screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
right_score = Scoreboard((100, 170))
left_score = Scoreboard((-100, 170))

screen.listen()

screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    # Detect collision with the paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.pong()
    # Detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        left_score.new_score()
    # Detect left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        right_score.new_score()



screen.exitonclick()