# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('Hirstspotpainting.jpg', 10)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r,g,b))
#
# print(rgb_colors)

import turtle as t
import random

number_of_dots = 100
color_list = [(144, 76, 50), (188, 165, 117), (166, 153, 36), (14, 46, 85), (139, 185, 176), (146, 56, 81)]
t.colormode(255)
timmy_the_turtle = t.Turtle()

timmy_the_turtle.hideturtle()
timmy_the_turtle.speed('fastest')
timmy_the_turtle.penup()
timmy_the_turtle.setheading(225)
timmy_the_turtle.forward(300)
timmy_the_turtle.setheading(0)

for dot_count in range(1, number_of_dots):
    timmy_the_turtle.pendown()
    timmy_the_turtle.dot(20, random.choice(color_list))
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(50)
    if dot_count % 10 == 0:
        timmy_the_turtle.setheading(90)
        timmy_the_turtle.forward(50)
        timmy_the_turtle.setheading(180)
        timmy_the_turtle.forward(500)
        timmy_the_turtle.setheading(0)

screen = t.Screen()
screen.exitonclick()