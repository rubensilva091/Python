import tkinter
from typing import Collection


root = tkinter.Tk()
root.title("Conversor Miles-KM")
root.minsize(width=170, height=80)
root.resizable(width=False, height=False)

var1 = tkinter.StringVar()
var1.set("0")

entry1 = tkinter.Entry(root, width=8)
entry1.grid(row=0, column=1)


label1 = tkinter.Label(root, text="is equal to", fg="black")
label1.grid(row=1, column=0)

label2 = tkinter.Label(root, text="Km", fg="black")
label2.grid(row=0, column=2)

label3 = tkinter.Label(root, text="Miles", fg="black")
label3.grid(row=1, column=2)

label4 = tkinter.Label(root, textvariable=var1, fg="black")
label4.grid(row=1, column=1)


def calculator1():
    variavel = int(entry1.get())
    variavel = 1.609344*variavel
    print(variavel)
    var1.set(str(variavel))


button1 = tkinter.Button(root, text="Calculate", fg="black",
                         command=calculator1)
button1.grid(row=2, column=1)


root.mainloop()
