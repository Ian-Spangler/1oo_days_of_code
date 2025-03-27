import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

car_manager = CarManager()

scoreboard = Scoreboard()

game_is_on = True
count = 1

screen.listen()

screen.onkey(player.move, "Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    # Create new car every 0.6 seconds
    if count == 6:
        count = 1
        car_manager.new_car()
    count += 1
    # Move every car
    car_manager.move()
    # Detect when the player collides with car
    for car in car_manager.cars:
        if car.distance(player) < 30:
            game_is_on = False
            scoreboard.game_over()
    # Detect when player reaches the top
    if player.goal():
        player.reset()
        car_manager.level_up()
        scoreboard.new_score()

screen.exitonclick()