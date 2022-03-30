from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("green")

# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
#
#
# tim.penup()
# tim.forward(350)
# tim.left(150)
# for _ in range(4):
#     tim.pendown()
#     tim.forward(150)
#     tim.left(120)
#     tim.penup()
#     tim.forward(50)
#     tim.left(60)
#     tim.pendown()
#     tim.forward(150)
#     tim.right(60)
#     tim.penup()
#     tim.forward(50)
#     tim.left(240)
#
# for _ in range(5):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#
# screen = Screen()
# screen.exitonclick()
#
# import heroes
# print(heroes.gen())

# angle = 360
# for i in range(3, 10):
#     ang = angle / i
#     for j in range(i):
#         tim.forward(100)
#         tim.right(ang)
import random

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

colours = ["red", "black", "blue", "violet", "yellow", "orange"]

for shape_side_n in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()



