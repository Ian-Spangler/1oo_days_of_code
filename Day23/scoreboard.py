from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-230, 260)
        self.write(f"Level: {self.level}", False, ALIGNMENT, FONT)

    def new_score(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", False, ALIGNMENT, FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, ALIGNMENT, FONT)