# from turtle import *
import turtle as t
import random


timmy_the_turtle = t.Turtle()
t.colormode(255)

# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("blue")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# # draw a square
# for i in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)
#

# # draw a dashed line
# for i in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

# # draw different shapes
# for i in range(3, 9):
#     for j in range(i):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(360/i)

# # draw random walk
# colors = ["medium slate blue", "dark orchid", "deep pink", "chartreuse", "dodger blue", "goldenrod", "medium spring green", "firebrick", "sienna", "indigo"]
# timmy_the_turtle.speed('fastest')
# timmy_the_turtle.pensize(10)
# for i in range(200):
#     timmy_the_turtle.pencolor(random.choice(colors))
#     timmy_the_turtle.right(random.randint(0,3)*90)
#     timmy_the_turtle.forward(20)

# # draw random walk with random RGB color
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)
# timmy_the_turtle.speed('fastest')
# timmy_the_turtle.pensize(10)
# for i in range(200):
#     timmy_the_turtle.pencolor(random_color())
#     timmy_the_turtle.right(random.randint(0,3)*90)
#     timmy_the_turtle.forward(20)

# draw a spirograph
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
timmy_the_turtle.speed('fastest')
number = random.randint(1, 100)
for i in range(number):
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.circle(100)
    timmy_the_turtle.setheading(timmy_the_turtle.heading() + 360 / number)

screen = t.Screen()
screen.exitonclick()