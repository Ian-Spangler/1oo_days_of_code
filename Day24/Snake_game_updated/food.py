from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super(). __init__()
        self.shape("circle")
        self.color("blue")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.new_food()

    def new_food(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
