from tkinter import *
import tkinter.font
from tkinter import messagebox
import math
import grafico


def fontConfig(n):
    return tkinter.font.Font(family="Comic Sans MS",
                                    size=n,
                                    weight="bold")


window = Tk()
window.title("Comp. Int. Calculator")
window.configure(bg='lightgrey')
window.geometry("400x700")
window.resizable(width=False, height=False)
#window.iconbitmap("logo.ico")

# Labels
titulo = Label(window, text="Calculator",
               font=fontConfig(28), bg="lightgrey", fg="darkorange")
titulo.place(x=110, y=0)

rodape = Label(window, text="PayPal: rubensilva091@gmail.com",
               font=fontConfig(12), bg="lightgrey")
rodape.place(x=135, y=673)


# Balanco Inicial
balancoInicial = Entry(window, width=30)
balancoInicial.place(x=15, y=107)
balancoInicial.insert(END, "0")
balancoInicialLabel = Label(
    window, text="Balanço Inicial", font=fontConfig(12), bg="lightgrey")
balancoInicialLabel.place(x=14, y=78)


# IR
interestRate = Entry(window, width=10)
interestRate.place(x=15, y=162)
interestRate.insert(END, "0")
interestRateLabel = Label(
    window, text="Interest Rate", font=fontConfig(12), bg="lightgrey")
interestRateLabel.place(x=14, y=133)


# IR Botaão
clickedIR = StringVar()
clickedIR.set("Yearly")

dropIR = OptionMenu(window, clickedIR,  "Daily",
                    "Weekly", "Monthly", "Yearly")
dropIR.place(x=150, y=155)


# Time Year
timeYear = Entry(window, width=10)
timeYear.place(x=15, y=217)
timeYear.insert(END, "0")
timeYearLabel = Label(
    window, text="Tempo (Anos)", font=fontConfig(12), bg="lightgrey")
timeYearLabel.place(x=14, y=188)


# Alguns Labels de Careteres
moedaLabel1 = Label(
    window, text="€", font=fontConfig(12), bg="lightgrey")
moedaLabel1.place(x=205, y=100)
moedaLabel2 = Label(
    window, text="€", font=fontConfig(12), bg="lightgrey")
moedaLabel2.place(x=205, y=332)
moedaLabel3 = Label(
    window, text="€", font=fontConfig(12), bg="lightgrey")
moedaLabel3.place(x=205, y=392)
percetagemLabel1 = Label(
    window, text="%", font=fontConfig(12), bg="lightgrey")
percetagemLabel1.place(x=85, y=155)

# CI
clickedCI = StringVar()
clickedCI.set("Monthly")

dropCI = OptionMenu(window, clickedCI,  "Daily", "Weekly", "Bi-Weekly", "Monthly",
                    "Bi-Monthly", "Quarterly",  "Half-Yearly", "Yearly")
dropCI.place(x=15, y=272)

compoundIntervalLabel = Label(
    window, text="Compound interval", font=fontConfig(12), bg="lightgrey")
compoundIntervalLabel.place(x=14, y=245)


# FINAL

finalTotalVAR = StringVar()
finalTotalVARIR = StringVar()
finalTotalVAR.set("0")
finalTotalVARIR.set("0")

finalTotalLabel = Label(
    window, text="Valor Final", font=fontConfig(20), bg="lightgrey")
finalTotalLabel.place(x=14, y=430)
finalTotalLabel = Label(
    window, textvariable=finalTotalVAR, font=fontConfig(20), bg="white", fg="blue")
finalTotalLabel.place(x=14, y=480)
finalTotalIRLabel = Label(
    window, text="Interest Rate", font=fontConfig(20), bg="lightgrey")
finalTotalIRLabel.place(x=14, y=540)
finalTotalIRLabel = Label(
    window, textvariable=finalTotalVARIR, font=fontConfig(20), bg="white", fg="darkorange")
finalTotalIRLabel.place(x=14, y=590)


# Deposito OM
clickedDeposit = StringVar()
clickedDeposit.set("Monthly")

# dropDeposit = OptionMenu(window, clickedDeposit,
# "Monthly", "Quarterly",  "Half-Yearly",  "Yearly")
dropDeposit = OptionMenu(window, clickedDeposit,
                         "Monthly", "...")
dropDeposit.place(x=240, y=330)


# Deposito
deposit = Entry(window, width=30)
deposit.place(x=15, y=337)
deposit.insert(END, "0")
depositLabelLabel = Label(
    window, text="Depositar", font=fontConfig(12), bg="lightgrey")
depositLabelLabel.place(x=14, y=308)


# Withdraw OM
clickedWithdraw = StringVar()
clickedWithdraw.set("Monthly")

# dropWithdraw = OptionMenu(window, clickedWithdraw,
# "Monthly", "Quarterly",  "Half-Yearly",  "Yearly")
dropWithdraw = OptionMenu(window, clickedWithdraw,
                          "Monthly", "...")
dropWithdraw.place(x=240, y=390)


# Withdraw
withdraw = Entry(window, width=30)
withdraw.place(x=15, y=397)
withdraw.insert(END, "0")
withdrawLabelLabel = Label(
    window, text="Retirar", font=fontConfig(12), bg="lightgrey")
withdrawLabelLabel.place(x=14, y=363)


# Butao Calcular
butaoCalcular = Button(window, text="Calcular", bd='5',
                       command=lambda: calcular(0))
butaoCalcular.place(x=315, y=485)

#Butão Grafico

butaoGrafico = Button(window,text="Grafico", bd='5',
                       command=lambda: calcular(1))
butaoGrafico.place(x=315, y=530)


def calcular(n1):
    p = int(balancoInicial.get())
    r = int(interestRate.get())/100
    t = int(timeYear.get())
    opcaoIR = leropcaoIR()
    r = r*opcaoIR
    n = leropcaoCI()
    nD = leropcaoDeposit()
    nW = leropcaoWithdraw()
    # pmt tem de ser sempre a dividir por 12!
    pmt = (int(deposit.get())*leropcaoDeposit()) - \
        (int(withdraw.get())*leropcaoWithdraw())
    # Formula da inflação anual
    #moeda = (moeda*(1+(t*a)-moeda)/moeda*(1+(t*a)))
    eq = (math.pow((1+(r/n)), (n*t)))
    # Formula final investimento inicial  -> A = P(1+r/n)^nt
    final1 = 1*(p*eq)
    # Formula final depositos regulares -> A = (PMT(1+r/n)^nt)/(r/n)
    final2 = pmt*(eq-1)/(r/n)
    final = final1 + final2
    if (n1==0):
        finalTotalVAR.set(str(round(final, 2))+" €")
        finalTotalVARIR.set(str(round(final-p-(pmt*t*12), 2))+" €")
    if (n1==1):
        grafico.graphFunction(p,r,n,t,pmt)


def leropcaoIR():
    opcao = clickedIR.get()
    if (opcao == "Yearly"):
        return 1
    elif (opcao == "Monthly"):
        return 12
    elif (opcao == "Weekly"):
        return 56
    elif (opcao == "Daily"):
        return 365


def leropcaoCI():
    opcao = clickedCI.get()
    if (opcao == "Yearly"):
        return 1
    elif (opcao == "Half-Yearly"):
        return 2
    elif (opcao == "Quarterly"):
        return 4
    elif (opcao == "Bi-Monthly"):
        return 6
    elif (opcao == "Monthly"):
        return 12
    elif (opcao == "Bi-Weekly"):
        return 26
    elif (opcao == "Weekly"):
        return 56
    elif (opcao == "Daily"):
        return 365


# porque o pmt tem de ser a dividir por 12
# def leropcaoDeposit():
  #  opcao = clickedDeposit.get()
   # if (opcao == "Yearly"):
   #     return 1/12
  #  elif (opcao == "Half-Yearly"):
   #     return 1/6
  #  elif (opcao == "Quarterly"):
  #      return 1/4
  #  elif (opcao == "Monthly"):
 #       return 1

def leropcaoDeposit():
    opcao = clickedDeposit.get()
    if (opcao == "Monthly"):
        return 1
    else:
        return 1

# porque o pmt tem de ser a dividir por 12


def leropcaoWithdraw():
    opcao = clickedWithdraw .get()
    if (opcao == "Monthly"):
        return 1
    else:
        return 1


window.mainloop()
