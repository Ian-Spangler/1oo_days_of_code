from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 72, "bold")

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.write(self.score, False, ALIGNMENT, FONT)

    def new_score(self):
        self.score += 1
        self.clear()
        self.write(self.score, False, ALIGNMENT, FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, ALIGNMENT, FONT)