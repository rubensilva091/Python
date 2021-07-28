from tkinter import *
from tkinter import messagebox
from calculator import *


def openWindow():
    window = Tk()
    window.title("Comp. Int. Calculator")
    window.configure(bg='lightgrey')
    window.geometry("400x700")
    window.resizable(width=False, height=False)
    window.iconbitmap("assets/logo.ico")
    calculator(window)
    window.mainloop()
    
