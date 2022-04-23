import time
from turtle import Screen

from player import Player
import car_manager
# from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
lev = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")

game_is_on = True

for car in range(car_manager.MOVE_INCREMENT):
    car = car_manager.CarManager()

while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player.ycor() >= player.FINISH_LINE_Y:
        player.reset_position()
        lev.increase_level()

