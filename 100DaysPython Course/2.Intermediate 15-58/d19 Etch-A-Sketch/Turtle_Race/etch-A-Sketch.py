import turtle


tim = turtle.Turtle()
root = turtle.Screen()
tim.penup()


# Criar as funçoes
def move_left():
    tim.backward(4)


def move_right():
    tim.forward(4)


def rotate_left():
    tim.right(4)


def rotate_right():
    tim.left(4)


def paint():
    tim.pendown()
    tim.forward(4)
    tim.penup()


def clear():
    tim.clear()
    tim.home()


# Mapear as funçoes no teclado
root.listen()
# isto nao estava a funcionar pois tem de ser funçoes e nao metodos
root.onkeypress(rotate_left, 'Left')
root.onkeypress(rotate_right, 'Right')
root.onkeypress(move_right, 'Up')
root.onkeypress(move_left, 'Down')
root.onkeypress(paint, 'space')
root.onkeypress(clear, 'c')


root.mainloop()
