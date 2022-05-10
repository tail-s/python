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
    answer_state = screen.textinput(title=f"{len(ansd_list)}/{len(state_list)} Guess the State", prompt="What's another state's name?").title() # title() 첫 글자를 대문자로

    if answer_state == "Exit":
        missing_states = [x for x in state_list if x not in ansd_list]
        # missing_states = []
        # for check in state_list:
        #     if check not in ansd_list:
        #         missing_states.append(check)

                # see = turtle.Turtle()
                # see.penup()
                # see.hideturtle()
                # see.goto(int(data[data.state == check].x), int(data[data.state == check].y))
                # see.write(check)

        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in state_list:
        ansd_list.append(answer_state)

        target_x = int(data[data.state == answer_state].x)
        target_y = int(data[data.state == answer_state].y)

        # item() 함수 기용 가능

        ans = turtle.Turtle()
        ans.penup()
        ans.hideturtle()
        ans.goto(target_x, target_y)
        ans.write(answer_state)

        if len(ansd_list) == len(state_list):
            game_is_on = False

    screen.update()

turtle.mainloop()

