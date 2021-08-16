import pandas
import turtle


EXCEL_FILE = "50_states.csv"
SHAPE_FILE = "blank_states_img.gif"


screen = turtle.Screen()
screen.title("States US")
screen.addshape(SHAPE_FILE)

turtle.shape(SHAPE_FILE)


data_stats = pandas.read_csv(EXCEL_FILE)
all_states = data_stats.state.to_list()


def get_coords_mouse_click(x, y):
    print(x, y)


turtle.onscreenclick(get_coords_mouse_click)


answer_state = screen.textinput(title="Guess the state", prompt="Name")


if answer_state in all_states:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data_stats [data_stats.state == answer_state]
    t.goto(int(state_data.x), int(state_data.y))
    t.write(answer_state)

screen.mainloop()
