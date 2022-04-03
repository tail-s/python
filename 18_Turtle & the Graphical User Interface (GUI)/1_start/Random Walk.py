import turtle as t
import random

t.colormode(255)
tim = t.Turtle()

tim.shape("turtle")
tim.color("black")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

direc = [0, 90, 180, 270]
tim.pensize(15)
tim.speed(7)

for _ in range(100):
    tim.color(random_color())
    dir = random.choice(direc)
    tim.setheading(dir)
    tim.forward(25)

screen = t.Screen()
screen.exitonclick()