from turtle import Turtle

MOVE_DISTANCE = 10



class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.left(90)
        self.shape("turtle")
        self.goto(x=0, y=-280)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def refresh(self):
        self.goto(x=0, y=-280)
