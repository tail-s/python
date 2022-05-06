import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
ansd_list = []

game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title=f"{len(ansd_list)}/{len(state_list)} Guess the State", prompt="What's another state's name?")

    if answer_state in state_list:
        ansd_list.append(answer_state)

        target_x = int(data[data.state == f"{answer_state}"].x)
        target_y = int(data[data.state == f"{answer_state}"].y)

        ans = turtle.Turtle()
        ans.penup()
        ans.hideturtle()
        ans.goto(target_x, target_y)
        ans.write(f"{answer_state}", align="center", font=("Courier", 10, "normal"))

        if len(ansd_list) == len(state_list):
            game_is_on = False

    screen.update()


turtle.mainloop()

