from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("black")

colours = ["red", "black", "blue", "violet", "orange"]
direc = [0, 90, 180, 270]

tim.pensize(15)
tim.speed(7)

for _ in range(150):
    dir = random.choice(direc)
    tim.color(random.choice(colours))
    tim.setheading(dir)
    tim.forward(25)

screen = Screen()
screen.exitonclick()