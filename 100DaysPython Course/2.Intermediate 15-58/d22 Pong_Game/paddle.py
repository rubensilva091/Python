import turtle


class Paddle(turtle.Turtle):
    # iniciar o paddle
    def __init__(self, inicialX, inicialY):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=inicialX, y=inicialY)

    # comando de subida

    def upward(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(), new_y)

    # comando de descida

    def downward(self):
        new_y = self.ycor()-20
        self.goto(self.xcor(), new_y)
