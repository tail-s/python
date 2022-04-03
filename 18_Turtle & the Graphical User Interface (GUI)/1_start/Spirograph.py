import turtle as t
import random

t.colormode(255)
a = t.Turtle()

a.pensize(1)
a.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw(num):
    angle = 360 / num
    for _ in range(num):
        a.color(random_color())
        a.circle(100)
        a.right(angle)

draw(15)

x = t.Screen()
x.exitonclick()


