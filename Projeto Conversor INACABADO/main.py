from tkinter import *
import tkinter.font
from tkinter import filedialog as fd
import mimetypes
from tkinter import messagebox
import math
from PIL import Image

pdf=('application/pdf', None)
word= ('application/vnd.openxmlformats-officedocument.wordprocessingml.document', None)
ico=('image/x-icon', None)
png=('image/png', None)
jpg=('image/jpeg', None)

def fontConfig(n):
    return tkinter.font.Font(family="Britannic Bold",
                                    size=n,
                                    weight="bold")

def change_color(n):
    if (n==1):
        indicador.configure(bg='green')
    else: 
        indicador.configure(bg='red')

root = Tk()

#Configuração da Janela inicial
root.title("Comp. Int. Calculator")
root.configure(bg='black')
root.geometry("200x300")
root.resizable(width=False, height=False)

#Titulo

titulo = Label(root, text="Conversor", font=fontConfig(30), bg="black", fg="green")
titulo.pack()

#Botao
pdfword= Button(root,text="PDF <-> WORD", bd='5', padx=39, pady= 5,
                       command=lambda: nada())
pdfword.pack()

pdfpng= Button(root,text="PDF <-> PNG", bd='5', padx=44, pady= 5,
                       command=lambda: nada())
pdfpng.pack()

pngjpg= Button(root,text="PNG <-> JPG", bd='5', padx=45, pady= 5,
                       command=lambda: nada())
pngjpg.pack()

pngico= Button(root,text="PNG <-> ICO", bd='5', padx=45, pady= 5,
                       command=lambda: nada())
pngico.pack()

abrirButton = Button(root, text='Open', command=lambda: loadFile(), bd="5",padx=30, pady= 5, bg="grey")
abrirButton.place(x=12,y=230)


#Indicador se está com ficheiro ou não

indicador = Canvas(root, width = 20, height = 20, bg="red")
indicador.place(x=146, y = 236) 


#usar em funçoes futuras
#indicador.bind('<1>', change_color(1))

def loadFile():
   file = fd.askopenfilename()
   tipoFile = mimetypes.guess_type(file)
   if (tipoFile==word or tipoFile==jpg or tipoFile==png or tipoFile == pdf or tipoFile == ico):
       change_color(1)
       print(file)
   else:
       file="0"
       change_color(0)
       messagebox.showinfo("Ficheiro nao suportado", "Esta app só suporta os ficheiros que estão representados nas Entry Box!\n\nTente de novo")

def nada():
    messagebox.showinfo("Não existe Ficheiro", "Não leu nenhum ficheiro de momento")

def pngjpg():
    print("LETS GO")
    #imagem = Image.open(file)
    #imagem.save(r'path where the JPG will be stored\new file name.jpg')
root.mainloop()