from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake = []
        self.new_snake()

    def new_snake(self):
        for position in STARTING_POSITIONS:
            snake_body = Turtle("square")
            snake_body.color("white")
            snake_body.penup()
            snake_body.goto(position)
            self.snake.append(snake_body)

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].goto(self.snake[i - 1].xcor(), self.snake[i - 1].ycor())
        self.snake[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake[0].heading() != DOWN:
            self.snake[0].setheading(UP)
            self.snake[0].forward(MOVE_DISTANCE)

    def down(self):
        if self.snake[0].heading() != UP:
            self.snake[0].setheading(DOWN)
            self.snake[0].forward(MOVE_DISTANCE)

    def left(self):
        if self.snake[0].heading() != RIGHT:
            self.snake[0].setheading(LEFT)
            self.snake[0].forward(MOVE_DISTANCE)

    def right(self):
        if self.snake[0].heading() != LEFT:
            self.snake[0].setheading(RIGHT)
            self.snake[0].forward(MOVE_DISTANCE)