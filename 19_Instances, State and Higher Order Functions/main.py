from turtle import Turtle, Screen
import random

# tim = Turtle()
is_race_on = False

screen = Screen()
screen.setup(width=500, height=400) # 숫자만 사용해도 됨
colors = ["red", "orange", "black", "green", "blue", "purple"]
all_turtles = []

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color (red/orange/black/green/blue/purple) : ")
print(f"Your Choice : {user_bet}")

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + turtle_index * 25)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            if turtle.pencolor() == user_bet:
                print(f"The winner is {turtle.pencolor()}. You've win!")
            else:
                print(f"The winner is {turtle.pencolor()}. You've lost!")

        mov = random.randint(0, 10)
        turtle.forward(mov)




# def fowards():
#     tim.forward(10)
# def backwards():
#     tim.backward(10)
# def counter_clockwise():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#     # tim.left(10)
# def clockwise():
#     tim.right(10)
# def clear_drawing():
#     # tim.reset()
#     tim.home()
#     tim.clear()
# screen.listen()
# screen.onkey(key="w", fun=fowards)
# screen.onkey(key="s", fun=backwards)
# screen.onkey(key="a", fun=counter_clockwise)
# screen.onkey(key="d", fun=clockwise)
# screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()
