import tkinter as tk
from tkinter.constants import TRUE
from typing import Text
from quiz_brain import *


THEME_COLOR = "#375362"
RIGHT_PNG = "d34 API_QUIZ\images\\true.png"
WRONG_PNG = "d34 API_QUIZ\images\\false.png"


class QuizUI():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # UI
        self.root = tk.Tk()
        self.root.title("Quizzler")
        self.root.config(padx=20, pady=20, bg=THEME_COLOR,
                         height=500, width=290)

        # Canvas
        self.canvas = tk.Canvas(width=300, height=250,
                                highlightthickness=0, borderwidth=0, bg="white")
        right = tk.PhotoImage(file=RIGHT_PNG)
        wrong = tk.PhotoImage(file=WRONG_PNG)
        self.text_UI = self.canvas.create_text(
            (150, 125), text="NOTHING RIGHT NOW", font=("Arial", 20, "bold"), width=260)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # buttons

        self.right_button = tk.Button(
            image=right, borderwidth=0, highlightthickness=0, command=lambda: self.true_pressed())
        self.right_button.grid(row=2, column=0)

        self.wrong_button = tk.Button(
            image=wrong, borderwidth=0, highlightthickness=0, command=lambda: self.false_pressed())
        self.wrong_button.grid(row=2, column=1)

        # label
        self.score_label = tk.Label(text="Score: 0", background=THEME_COLOR, font=(
            "Arial", 15, "italic"), fg="white")
        self.score_label.grid(row=0, column=1)


        self.next_question_GUI()
        
        self.root.mainloop()

    def next_question_GUI(self):
        if (self.quiz.still_has_questions() == True):
          self.question = self.quiz.next_question()
          self.canvas.itemconfig(self.text_UI, text=self.question)
        else:
          self.canvas.itemconfig(self.text_UI, text="OVER")

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text_UI, text=q_text)
        else:
            self.canvas.itemconfig(self.text_UI, text="You've reached the end of the quiz.")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.root.after(1000, self.get_next_question)
