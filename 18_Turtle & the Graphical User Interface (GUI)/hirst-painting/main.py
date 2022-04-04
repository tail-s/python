# import colorgram
#
# num_of_color = 20
# colors = colorgram.extract('hirst.jpg', num_of_color)
# rgb_colors = []
# for color in colors:
#     # rgb_colors.append(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_data = (r, g, b)
#     rgb_colors.append(color_data)
#
# print(rgb_colors)
# 색상정보 추출

import turtle as t
import random

t.colormode(255)
colors = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151)]

d = t.Turtle()
d.speed("fastest")
d.hideturtle()

def hirst(num):
    for i in range(num):
        for j in range(num):
            d.penup()
            d.goto(65 * j, 65 * i)
            d.pendown()
            color = random.choice(colors)
            d.dot(20, color)

hirst(5)

x = t.Screen()
x.exitonclick()




