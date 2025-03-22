# Turtle race bet
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue"]
y_positions = [-70, -40, -10, 20, 50]
is_race_on = False
turtles = []
winner = ""

for i in range(0, 5):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-230, y_positions[i])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for t in turtles:
        rand_distance = random.randint(0,10)
        t.forward(rand_distance)
        if t.xcor() > 230:
            is_race_on = False
            winner = t.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
screen.listen()
screen.exitonclick()