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



class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        # self.colormode(mode=255)
        self.penup()
        self.STARTING_MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 10

    def cars_ready(self):

        cars = []
        for car in range(0, self.MOVE_INCREMENT):
            car = CarManager()
            car.color(COLORS[random.randint(0, len(COLORS) - 1)])
            target_x = random.randint(0, 300)
            target_y = random.randint(0, 600)
            car.goto(target_x, target_y)
            car.setheading(180)
            car.forward(self.STARTING_MOVE_DISTANCE)
            cars.append(car)

            if car.xcor() == -320:
                car.goto(target_x, 320)

