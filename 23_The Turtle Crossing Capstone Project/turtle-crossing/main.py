import time
from turtle import Screen

import player
# from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

play = player.Player()
car = CarManager()
lev = Scoreboard()

screen.listen()
screen.onkey(play.up, "Up")
screen.onkey(play.down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    if play.ycor() >= player.FINISH_LINE_Y:
        play.reset_position()
        lev.increase_level()

