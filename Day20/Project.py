# Snake Game
from turtle import Turtle, Screen
import time
import random

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)
snake = []
game_is_on = True

def snake_body_layout():
    snake[1].goto(snake[0].xcor()-20, 0)
    snake[2].goto(snake[1].xcor()-20, 0)



for i in range(0, 3):
    snake_body = Turtle("square")
    snake_body.color("white")
    snake_body.penup()
    snake.append(snake_body)

snake_body_layout()


while game_is_on:
    screen.update()
    time.sleep(0.1)
    for s in snake:
        s.forward(20)

screen.listen()
screen.exitonclick()