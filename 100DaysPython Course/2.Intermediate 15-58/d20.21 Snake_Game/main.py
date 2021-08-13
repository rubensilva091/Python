import random
import turtle
import time


class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font="Arial")

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font="Arial")

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


# deveria ter feito isto para a cobra principal, mas agora Ce la vie
class Food(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)


# Não é preciso init, pois o turtle.Turtle() Já é uma class !! ! !! !
SNAKE_INICIAL_SIZE = 4

# window
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(600, 600)
screen.tracer(0)  # desligar animações


snake = []  # list of entire body of the snake
scoreboard = Scoreboard()
food = Food()

# def Functions


def upward():
    rot = 90
    if (cant_backwards(rot, 0) == 1):
        snake[0].setheading(rot)


def rightward():
    rot = 0
    if (cant_backwards(rot, 1) == 1):
        snake[0].setheading(rot)


def downward():
    rot = 270
    if (cant_backwards(rot, 2) == 1):
        snake[0].setheading(rot)


def leftward():
    rot = 180
    if (cant_backwards(rot, 3) == 1):
        snake[0].setheading(rot)


# Proibir cobra andar para tras
def cant_backwards(rot, dir):
    if((dir == 0 and (snake[0].heading() == 270)) or (dir == 1 and (snake[0].heading() == 180) or (dir == 2 and (snake[0].heading() == 90) or (dir == 3 and (snake[0].heading() == 0))))):
        return 0
    return 1


# Construtor de Cobras
def create_body(var):
    for i in range(var):
        snakePixel = turtle.Turtle()
        snakePixel.speed("slow")
        snakePixel.penup()
        snakePixel.shape("square")
        snakePixel.color("white")
        snake.append(snakePixel)


# Mapping Functions
screen.listen()
screen.onkey(upward, "Up")
screen.onkey(rightward, "Right")
screen.onkey(downward, "Down")
screen.onkey(leftward, "Left")


# Mover a Cobra
def moveSnake():
    for i in range(len(snake)-1, 0, -1):
        new_x = snake[i-1].xcor()
        new_y = snake[i-1].ycor()
        snake[i].goto(x=new_x, y=new_y)
    snake[0].forward(20)


# Colisão
def collision():
    if (collision_map() == 0 or collision_snake() == 0):
        return 0
    return 1


def collision_map():
    if (snake[0].xcor() > 300 or snake[0].xcor() < -300 or snake[0].ycor() > 300 or snake[0].ycor() < -300):
        return 0
    return 1


# tenho de melhorar!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def collision_snake():
    if(len(snake) > SNAKE_INICIAL_SIZE):
        for i in range(1, len(snake)):
            head_x = snake[0].xcor()
            head_y = snake[0].ycor()
            if (head_x == snake[i].xcor() and head_y == snake[i].ycor()):
                return 0
        return 1


# tenho de acacabr!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def collision_food():
    if (snake[0].distance(food) < 15):
        create_body(1)
        #isto não funciona nao sei o pq, deepois vejo
        scoreboard.increase_score()
        food.refresh()


def scoreboard():
    snake[0].write("Home= ", True, align="center")

# Função para Jogar


def play():
    create_body(SNAKE_INICIAL_SIZE)
    while(True):
        screen.update()
        if (collision() == 0):
            break
        collision_food()
        time.sleep(0.1)  # dar delay ao jogo para não ser tao rapido
        moveSnake()
        


play()


screen.mainloop()
