import turtle
import pandas

screen = turtle.Screen()
screen.title("Guess the state name")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

guessed_states = []
learn_states = []

data = pandas.read_csv("50_states.csv")
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"Guess the state {len(guessed_states)}/50",
                                    prompt="Enter another state name:").title()
    if answer_state == "Exit":
        learn_states = [state for state in data.state if state not in guessed_states]

        new_file = pandas.DataFrame(learn_states, columns=["learn these states"])
        new_file.to_csv("learn_states.csv")
        break

    for curr_state in data["state"]:

        if answer_state == curr_state:

            state_row = data[data["state"] == curr_state]
            x_corr = int(state_row["x"])
            y_corr = int(state_row["y"])
            writer.goto(x_corr, y_corr)
            writer.write(arg=curr_state, align="center")
            guessed_states.append(curr_state)







screen.clear()
# screen.exitonclick()
#the below life is alternative of the above line and keeps the screen open always
screen.mainloop()
