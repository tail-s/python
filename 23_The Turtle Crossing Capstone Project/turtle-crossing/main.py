import time
from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
lev = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")

for cars in range(0, car.MOVE_INCREMENT):
    new_car = CarManager()
    target_x = random.randint(0, 300)
    target_y = random.randint(0, 600)
    new_car.goto(target_x, target_y)
    new_car.setheading(180)
    new_car.forward(car.STARTING_MOVE_DISTANCE)
    cars.append(new_car)

    if cars.new_car.xcor() == -320:
        new_car.goto(target_x, 320)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player.clear():
        lev.increase_level()

