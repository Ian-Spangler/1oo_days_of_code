import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_is_on = True
data = pandas.read_csv("50_states.csv")
name_data = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer == "Exit":
        missing_states = []
        for name in name_data:
            if name not in guessed_states:
                missing_states.append(name)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    for name in name_data:
        if name == answer:
            t = turtle.Turtle()
            t.penup()
            t.hideturtle()
            t.goto(int(data[data["state"] == answer].x), int(data[data["state"] == answer].y))
            t.write(answer)
            guessed_states.append(answer)
screen.exitonclick()
