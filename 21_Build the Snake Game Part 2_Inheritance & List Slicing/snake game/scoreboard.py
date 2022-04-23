from turtle import Turtle
from food import Food

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("Game Over", align=ALIGNMENT, font=("Courier", 60, "normal")) # clear를 사용하지 않기에 기존 점수판은 남아있지!

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

