from turtle import Turtle, Screen

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segment = []
        self.new_snake()
        self.snake_head = self.segment[0]

    def new_snake(self):
        for position in STARTING_POSITIONS:
            snake_body = Turtle("square")
            snake_body.color("white")
            snake_body.penup()
            snake_body.goto(position)
            self.segment.append(snake_body)

    def add_segment(self, position):
        snake_body = Turtle("square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.goto(position)
        self.segment.append(snake_body)

    def extend_snake(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for i in range(len(self.segment) - 1, 0, -1):
            self.segment[i].goto(self.segment[i - 1].xcor(), self.segment[i - 1].ycor())
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)
            self.snake_head.forward(MOVE_DISTANCE)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)
            self.snake_head.forward(MOVE_DISTANCE)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)
            self.snake_head.forward(MOVE_DISTANCE)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
            self.snake_head.forward(MOVE_DISTANCE)