import time
from turtle import Screen, onkeypress
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

PROB = 10  # probabilidade de 1 em PROB de spawnar um carro

# screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

game_is_on = True

# objects
player = Player()
scoreboard = Scoreboard()
enemy_car = CarManager()

# events
screen.listen()
onkeypress(player.move, "Up")


# game Functions
def level_done():
    if (player.ycor() > 280):
        player.refresh()
        scoreboard.level_up()
        enemy_car.car_level_up()


# colisao
def collision_enemy():
    for car in enemy_car.enemys:
        if (car.distance(player) < 20):
            return 1
    return 0


# Game
while (True):
    time.sleep(0.1)
    level_done()
    enemy_car.move_enemys()
    probz = random.randint(1, PROB)
    if (probz == 1):
        enemy_car.create_new_enemy()
    if (collision_enemy() != 0):
        scoreboard.game_over()
        break
    screen.update()

screen.mainloop()
