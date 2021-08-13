import turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()  # limpar a antiga scoreboard
        self.goto(-220, 260)
        self.write("Level: "+str(self.level), align="Center",
                   font=("Courier", 20, "normal"))

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game OVER!", align="Center",
                   font=("Courier", 60, "normal"))
