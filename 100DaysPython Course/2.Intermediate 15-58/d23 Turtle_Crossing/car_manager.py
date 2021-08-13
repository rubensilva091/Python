from hashlib import new
from turtle import Turtle, hideturtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()  # tirar um ponto estupido no meio do ecra
        self.enemys = []
        self.var_speed = 10
        self.create_new_enemy()

    def create_new_enemy(self):
        new_enemy = Turtle("square")
        new_enemy.color(random.choice(COLORS))
        new_enemy.penup()
        new_enemy.shapesize(stretch_len=2)
        new_enemy.left(180)  # rodar-los todos para esquerda
        new_y = random.randint(-200, 200)
        new_enemy.goto(x=300, y=new_y)
        self.enemys.append(new_enemy)

    def move_enemys(self):
        for i in self.enemys:
            if (i.xcor() > -350):
                i.forward(self.var_speed)
            else:
                self.enemys.remove(i)
                # limpar o precessamento da lista,
                # elas vao continuar aparecer na tela, mas não serão
                # processadas!!!
                # para evitar futuros problemas

    def car_level_up(self):
        self.var_speed += MOVE_INCREMENT
