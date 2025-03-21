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

color_list = [(144, 76, 50), (188, 165, 117), (248, 244, 246), (166, 153, 36), (14, 46, 85), (139, 185, 176), (146, 56, 81)]
t.colormode(255)
timmy_the_turtle = t.Turtle()

for i in range(5):
    for j in range(5):
        timmy_the_turtle.pendown()
        timmy_the_turtle.dot(20, random.choice(color_list))
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(50)


screen = t.Screen()
screen.exitonclick()