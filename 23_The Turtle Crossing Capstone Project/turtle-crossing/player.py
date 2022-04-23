from turtle import Turtle

STARTING_POSITION = (0, -280)


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.reset_position()
        self.MOVE_DISTANCE = 10
        self.FINISH_LINE_Y = 280

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def up(self):
        new_y = self.ycor() + self.MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - self.MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
