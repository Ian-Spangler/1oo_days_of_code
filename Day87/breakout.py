import turtle
import time

screen = turtle.Screen()
screen.title("Breakout Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

def paddle_left():
    x = paddle.xcor()
    if x > -350:
        paddle.setx(x - 40)

def paddle_right():
    x = paddle.xcor()
    if x < 350:
        paddle.setx(x + 40)

screen.listen()
screen.onkeypress(paddle_left, "Left")
screen.onkeypress(paddle_right, "Right")

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, -200)
ball.dx = 4
ball.dy = 4

bricks = []

colors = ["red", "orange", "yellow", "green"]

start_x = -360
start_y = 250

total_rows = 7

for row in range(total_rows):
    for col in range(12):
        brick = turtle.Turtle()
        brick.speed(0)
        brick.shape("square")
        brick.color(colors[row//(total_rows//4+1)])
        brick.shapesize(stretch_wid=1, stretch_len=3)
        brick.penup()
        brick.goto(start_x + col * 65, start_y - row * 25)
        bricks.append(brick)

score = 0

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0, 260)
score_pen.write("Score: 0", align="center", font=("Arial", 16, "normal"))

game_running = True

while game_running:
    screen.update()
    time.sleep(0.016)

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.dy *= -1

    if (
        -260 < ball.ycor() < -240
        and paddle.xcor() - 60 < ball.xcor() < paddle.xcor() + 60
    ):
        ball.dy *= -1

    for brick in bricks[:]:
        if ball.distance(brick) < 35:
            brick.hideturtle()
            bricks.remove(brick)
            ball.dy *= -1
            score += 10
            score_pen.clear()
            score_pen.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))

    if ball.ycor() < -300:
        score_pen.goto(0, 0)
        score_pen.write("GAME OVER", align="center", font=("Arial", 30, "bold"))
        game_running = False

    if not bricks:
        score_pen.goto(0, 0)
        score_pen.write("YOU WIN!", align="center", font=("Arial", 30, "bold"))
        game_running = False

screen.mainloop()
