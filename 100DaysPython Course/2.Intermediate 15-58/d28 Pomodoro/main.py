import tkinter as tk
import math
from typing import Text


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TOMATO_PNG = "d28 Pomodoro\\tomato.png"
FONT = (FONT_NAME, 35, "bold")
reps = 0
timer_loop = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    timer.config(fg=GREEN, text="Timer")
    visto.config(text=" ")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    root.after_cancel(timer_loop)


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    if (reps == 1 or reps == 3 or reps == 5 or reps == 7):
        timer.config(fg=GREEN, text="Timer")
        countdown_func(WORK_MIN*60-1)
    elif(reps == 8):
        timer.config(fg=RED, text="Long Break")
        break_time(LONG_BREAK_MIN*60-1)  # ultimo break

        reset()  # tenho de colocar aqui o reset

    elif(reps == 2 or reps == 4 or reps == 6):
        timer.config(fg=PINK,  text="Break")
        break_time(SHORT_BREAK_MIN*60-1)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
session_count = []


def countdown_func(count):

    count_min = math.floor(count/60)
    count_sec = count % 60

    min_display = str(count_min)
    sec_display = str(count_sec)

    # Não perder os 4 digitos do counter (04:01) por exemplo
    if (count_min < 10):
        min_display = "0"+str(count_min)

    if (count_sec < 10):
        sec_display = "0"+str(count_sec)

    canvas.itemconfig(timer_text, text=f"{min_display}:{sec_display}")
    if count > 0:
        global timer_loop
        timer_loop = root.after(1000, countdown_func, count-1)  # recursividade


def break_time(count):
    countdown_func(count)
    increment_visto()


def increment_visto():
    session_count.append("1")  # incrementar a lista
    string = " "
    for i in session_count:
        string += "✔"
    visto.config(text=string)


# ---------------------------- UI SETUP ------------------------------- #


# Screen
root = tk.Tk()
root.title("Pomodoro APP")
root.resizable(width=False, height=False)
root.config(padx=100, pady=50, bg=YELLOW)


# Canvas
img = tk.PhotoImage(file=TOMATO_PNG)  # abrir imagem
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white",
                                font=FONT)
canvas.grid(row=1, column=1)


# Timer Label
timer = tk.Label(root, text="Timer", font=FONT, bg=YELLOW, fg=GREEN)
timer.grid(row=0, column=1)


# Start Button
start = tk.Button(root, text="Start",
                  command=start_timer, highlightthickness=0)
start.grid(row=2, column=0)


# Reset Button
reset = tk.Button(root, text="Reset", command=reset_timer,
                  highlightthickness=0)
reset.grid(row=2, column=2)


# Visto Label
visto = tk.Label(root, text=" ", font=(FONT_NAME, 20), bg=YELLOW, fg=GREEN)
visto.grid(row=3, column=1)


root.mainloop()
