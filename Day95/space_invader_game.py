import turtle
import random
import math
import time

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.setup(width=800, height=600)
wn.tracer(0)

score = 0

score_pen = turtle.Turtle()
score_pen.hideturtle()
score_pen.color("white")
score_pen.penup()
score_pen.goto(-380, 260)
score_pen.write("Score: 0", font=("Arial", 14, "normal"))

player = turtle.Turtle()
player.shape("triangle")
player.color("white")
player.penup()
player.setheading(90)
player.goto(0, -250)

player_speed = 20

def move_left():
    x = player.xcor()
    if x > -380:
        player.setx(x - player_speed)

def move_right():
    x = player.xcor()
    if x < 380:
        player.setx(x + player_speed)

bullet = turtle.Turtle()
bullet.shape("square")
bullet.color("yellow")
bullet.penup()
bullet.shapesize(stretch_wid=0.2, stretch_len=1)
bullet.setheading(90)
bullet.hideturtle()

bullet_speed = 25
bullet_state = "ready"

def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        bullet.goto(player.xcor(), player.ycor() + 10)
        bullet.showturtle()

enemies = []
num_enemies = 8
enemy_speed = 2
enemy_drop = 30

for _ in range(num_enemies):
    enemy = turtle.Turtle()
    enemy.shape("circle")
    enemy.color("green")
    enemy.penup()
    x = random.randint(-300, 300)
    y = random.randint(100, 250)
    enemy.goto(x, y)
    enemies.append(enemy)

def is_collision(t1, t2):
    distance = math.sqrt(
        (t1.xcor() - t2.xcor()) ** 2 +
        (t1.ycor() - t2.ycor()) ** 2
    )
    return distance < 20

wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(fire_bullet, "space")

game_over = False

while not game_over:
    wn.update()

    if bullet_state == "fire":
        bullet.sety(bullet.ycor() + bullet_speed)

    if bullet.ycor() > 300:
        bullet.hideturtle()
        bullet_state = "ready"

    move_down = False
    for enemy in enemies:
        enemy.setx(enemy.xcor() + enemy_speed)

        if enemy.xcor() > 380 or enemy.xcor() < -380:
            move_down = True

        if is_collision(bullet, enemy):
            bullet.hideturtle()
            bullet_state = "ready"
            bullet.goto(0, -400)

            enemy.goto(random.randint(-300, 300), random.randint(150, 250))
            score += 10
            score_pen.clear()
            score_pen.write(f"Score: {score}", font=("Arial", 14, "normal"))

        if is_collision(player, enemy):
            game_over = True

    if move_down:
        for enemy in enemies:
            enemy.sety(enemy.ycor() - enemy_drop)
        enemy_speed *= -1

    time.sleep(0.02)

game_pen = turtle.Turtle()
game_pen.color("red")
game_pen.penup()
game_pen.hideturtle()
game_pen.goto(0, 0)
game_pen.write("GAME OVER", align="center", font=("Arial", 36, "bold"))

wn.mainloop()
