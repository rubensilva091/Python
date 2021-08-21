import tkinter as tk
import pandas
import random
import time


BACKGROUND_COLOR = "#B1DDC6"
GREEN_CARD_COLOR = "#91c2af"
CARD_BACK_PNG = "d31 Flash_Card\images\card_back.png"
CARD_FRONT_PNG = "d31 Flash_Card\images\card_front.png"
RIGHT_PNG = "d31 Flash_Card\images\\right.png"
WRONG_PNG = "d31 Flash_Card\images\wrong.png"
WORDS_CSV = "d31 Flash_Card\data\\french_words.csv"
NEW_CSV = "d31 Flash_Card\data\\words_to_learn.csv"


# Inicializar
try:
    open(NEW_CSV, "r")
except:
    data = pandas.read_csv(WORDS_CSV)
    words = data.to_dict(orient="records")
else:
    data = pandas.read_csv(NEW_CSV)
    words = data.to_dict(orient="records")


def main_funct(aux):

    update_image(image_front_card)
    language_label.config(fg="black", bg="white")
    word_label.config(fg="black", bg="white")
    word_english.set(aux["French"])
    language_english.set("French")
    root.update()
    time.sleep(3)

    update_image(image_back_card)
    language_label.config(fg="white", bg=GREEN_CARD_COLOR)
    word_label.config(fg="white", bg=GREEN_CARD_COLOR)
    word_english.set(aux["English"])
    language_english.set("English")
    root.update()


def update_image(img2):
    card_bg.itemconfig(card_image, image=img2)


def wrong():
    aux = random.choice(words)
    main_funct(aux)


def right():
    aux = random.choice(words)
    words.remove(aux)
    new_data = pandas.DataFrame(words)
    new_data.to_csv(NEW_CSV)
    main_funct(aux)


# UI---------------
# Window
root = tk.Tk()
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
root.title("Flashy")


# Open PNG
image_front_card = tk.PhotoImage(file=CARD_FRONT_PNG)
image_back_card = tk.PhotoImage(file=CARD_BACK_PNG)
right_png = tk.PhotoImage(file=RIGHT_PNG)
wrong_png = tk.PhotoImage(file=WRONG_PNG)


# canvas
card_bg = tk.Canvas(width=800, height=526,
                    bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = card_bg.create_image(400, 263, image=image_front_card)
card_bg.grid(row=0, column=0, columnspan=2)


# StringVar

word_english = tk.StringVar()
language_english = tk.StringVar()

word_english.set("Word")
language_english.set("Language")

# Labels

language_label = tk.Label(font=("Ariel", 30, "italic"),
                          textvariable=language_english, highlightthickness=0, bg="white")
language_label.place(x=300, y=100)


word_label = tk.Label(font=("Ariel", 50, "bold"),
                      textvariable=word_english, highlightthickness=0, bg="white")
word_label.place(x=250, y=243)


# buttons
wrong_button = tk.Button(
    image=wrong_png, highlightthickness=0, borderwidth=0, command=wrong)
wrong_button.grid(row=1, column=0)

right_button = tk.Button(
    image=right_png, highlightthickness=0,  borderwidth=0, command=right)
right_button.grid(row=1, column=1)


root.mainloop()
