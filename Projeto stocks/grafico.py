from tkinter import *

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import math
import numpy as np

def graphFunction(p,r,n,t,pmt):
    window = Tk()
    window.wm_title("Grafico de Crescimento")
    window.iconbitmap("assets/logo.ico")
    window.resizable(width=False, height=False)
    window.geometry("600x500")

    def f(x):
     return (p*(math.pow((1+(r/n)), (n*x))))+(pmt*((math.pow((1+(r/n)), (n*x))-1)/(r/n)))
    
    f2 = np.vectorize(f)
    fig = Figure(figsize=(5, 4), dpi=100)
    x = np.arange(0, t, 0.01) #(Inicio, Fim, precisão)


    fig.add_subplot(111).plot(x, f2(x)) #(variavel em estudo, função)

    canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    def on_key_press(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, canvas, toolbar)


    canvas.mpl_connect("key_press_event", on_key_press)
    window.mainloop()

    