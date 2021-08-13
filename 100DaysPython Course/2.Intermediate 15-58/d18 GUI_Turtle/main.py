from turtle import *
import turtle
import random
from typing import Counter
import cores

COLOR1 = "black"
COLOR2 = "green"
X = 500
Y = 500

screen = Screen()
screen.screensize(canvheight=X, canvwidth=Y, bg=COLOR1)
colormode(255)

timmy_the_turtle = Turtle()
timmy_the_turtle.color(COLOR2)


# challenge 5
def random_color():
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    random_color = (r, g, b)
    return random_color


# challenge 1
def challenge_1():
    for i in range(4):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(90)


# challenge 2
# Minha resolução
def challenge_2_0():
    for i in range(20):
        timmy_the_turtle.forward(10)
        timmy_the_turtle.color(COLOR1)
        timmy_the_turtle.forward(10)
        timmy_the_turtle.color(COLOR2)


# Resolução original
def challenge_2_1():
    for i in range(20):
        timmy_the_turtle.forward(10)
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(10)
        timmy_the_turtle.pendown()


# Angulos:
# Triangulo (3)(60),
# Quadrado(4)(90),
# Pentagono(5)(108),
# Hexagono(6)(120),
# Heptagono(7)(128.57),
# Octogono(8)(135),
# Eneagono(9)(140),
# Decagono(10)(144).
lados = [3, 4, 5, 6, 7, 8, 9, 10]
angulos = [60, 90, 108, 120, 128.57, 135, 140, 144]


# Minha resolução
def challenge_3_0():
    counter = 0
    for i in angulos:
        timmy_the_turtle.color(random_color())
        for y in range(0, lados[counter]):
            timmy_the_turtle.forward(100)
            timmy_the_turtle.left(i+180)
        counter += 1


# Resolução original
def challenge_3_1():
    def draw_shape(num_sides):
        angle = 360 / num_sides
        for _ in range(num_sides):
            timmy_the_turtle.forward(100)
            timmy_the_turtle.right(angle)

    for shape_side_n in range(3, 10):
        timmy_the_turtle.color(random_color())
        draw_shape(shape_side_n)


# Minha Resolução
def challenge_4_0():
    timmy_the_turtle.pensize(15)
    timmy_the_turtle.speed("fastest")
    for i in range(200):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.right(90*random.randrange(0, 3))
        timmy_the_turtle.forward(30)


# Resolução original
def challenge_4_1():
    directions = [0, 90, 180, 270]
    timmy_the_turtle.pensize(15)
    timmy_the_turtle.speed("fastest")

    for _ in range(200):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.forward(30)
        timmy_the_turtle.setheading(random.choice(directions))


# Minha Resolução
def challenge_5_0():
    counter = 0
    rotation = 1
    timmy_the_turtle.speed("fastest")
    while(True):
        if (counter >= 360):
            break
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.right(rotation)
        timmy_the_turtle.circle(150)
        counter += rotation


# Minha Resolução
def challenge_final_0():
    timmy_the_turtle.penup()
    timmy_the_turtle.setheading(225)
    timmy_the_turtle.forward(300)
    timmy_the_turtle.setheading(0)
    number_of_dots = 100

    for i in range(1, number_of_dots + 1):
        timmy_the_turtle.dot(20, random_color())
        timmy_the_turtle.forward(50)

        if (i % 10 == 0):
            timmy_the_turtle.setheading(90)
            timmy_the_turtle.forward(50)
            timmy_the_turtle.setheading(180)
            timmy_the_turtle.forward(500)
            timmy_the_turtle.setheading(0)


challenge_5_0()

screen.mainloop()
