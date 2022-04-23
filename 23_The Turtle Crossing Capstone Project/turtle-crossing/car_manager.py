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

# COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
import turtle
import random

COLORS = [(163, 209, 243), (247, 199, 221), (167, 247, 209), (252, 236, 205)]

MOVE_INCREMENT = 10
STARTING_MOVE_DISTANCE = 5
turtle.colormode(255)

class CarManager:

    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = turtle.Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
