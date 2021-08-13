import turtle


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.p1_score = 0
        self.p2_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()  # limpar a antiga scoreboard
        self.goto(-100, 200)
        self.write(self.p1_score, align="Center",
                   font=("Courier", 70, "normal"))
        self.goto(100, 200)
        self.write(self.p2_score, align="Center",
                   font=("Courier", 70, "normal"))

    def p_score(self, player):
        if (player == 1):
            self.p1_score += 1
        if (player == 2):
            self.p2_score += 1
        self.update_scoreboard()
