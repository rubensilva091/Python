import turtle


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.goto(x=0, y=0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed=0.1
        self.penup()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self, direction):
        if (direction == "vertical"):
            self.y_move = -(self.y_move)
        if (direction == "horizontal"):
            self.move_speed*=0.9
            self.x_move = -(self.x_move)

    def refresh(self):
        self.goto(x=0, y=0)
        self.move_speed=0.1
        self.bounce("horizontal")

