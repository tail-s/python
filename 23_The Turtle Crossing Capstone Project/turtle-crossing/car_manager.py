# import colorgram
#
# num_of_color = 4
# colors = colorgram.extract('./color.jpg', num_of_color)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_data = (r, g, b)
#     rgb_colors.append(color_data)
#
# print(rgb_colors)

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

from turtle import Turtle
import random

# COLORS = [(163, 209, 243), (247, 199, 221), (167, 247, 209), (252, 236, 205)]

MOVE_INCREMENT = 10
STARTING_MOVE_DISTANCE = 5

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(COLORS[random.randint(0, len(COLORS) - 1)])
        self.penup()
        self.target_x = random.randint(0, 300)
        self.target_y = random.randint(-250, 250)
        self.goto(self.target_x, self.target_y)
        self.setheading(180)
        if self.xcor() == -320:
            self.goto(self.target_x, 320)



