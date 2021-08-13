import turtle
from paddle import *
from ball import *
from scoreboard import *
import time

# configurar screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


# Objects
paddle1 = Paddle(350, 0)   # P1
paddle2 = Paddle(-350, 0)  # P2
ball = Ball()              # Bola
scoreboard = Scoreboard()


screen.listen()
# P1
screen.onkey(paddle1.upward, "Up")
screen.onkey(paddle1.downward, "Down")


# P2
screen.onkey(paddle2.upward, "w")
screen.onkey(paddle2.downward, "s")


# Colisão Vertical
def collision_vertical():
    direction = "vertical"
    y_ball = ball.ycor()
    if (y_ball > 270 or y_ball < -270):
        ball.bounce(direction)


def collision_paddle():
    direction = "horizontal"
    x_ball = ball.xcor()
    paddle1_distance = ball.distance(paddle1)
    paddle2_distance = ball.distance(paddle2)
    right_limit = 330
    left_limit = -330
    if ((x_ball > right_limit and paddle1_distance < 50) or (x_ball < left_limit and paddle2_distance < 50)):
        ball.bounce(direction)



def score():
    x_ball = ball.xcor()
    paddle1_distance = ball.distance(paddle1)
    paddle2_distance = ball.distance(paddle2)
    right_limit = 330
    left_limit = -330
    if (x_ball > right_limit and paddle1_distance > 50):
        ball.refresh()
        scoreboard.p_score(1)
    if (x_ball < left_limit and paddle2_distance > 50):
        ball.refresh()
        scoreboard.p_score(2)



while(True):
    time.sleep(ball.move_speed)
    ball.move()
    collision_vertical()
    collision_paddle()
    score()
    screen.update()
