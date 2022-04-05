from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def fowards():
    tim.forward(10)

def backwards():
    tim.backward(10)

def counter_clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    # tim.left(10)

def clockwise():
    tim.right(10)

def clear_drawing():
    # tim.reset()
    tim.home()
    tim.clear()

screen.listen()
screen.onkey(key="w", fun=fowards)
screen.onkey(key="s", fun=backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()
