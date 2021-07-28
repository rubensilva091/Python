from tkinter import *
import tkinter.font
from tkinter import messagebox
from calculatorScript import *


def fontConfig(n):
    return tkinter.font.Font(family="Comic Sans MS",
                                    size=n,
                                    weight="bold")


def fontConfigColor1(n):
    return tkinter.font.Font(family="Comic Sans MS",
                                    size=n,
                                    weight="bold")


def calculator(window):
    labelsMAIN(window)
    inputData(window)
    calcularButton(window)


def labelsMAIN(window):
    titulo = Label(window, text="Calculator",
                   font=fontConfig(28), bg="lightgrey", fg="darkorange")
    titulo.place(x=110, y=0)

    rodape = Label(window, text="PayPal: rubensilva091@gmail.com",
                   font=fontConfig(12), bg="lightgrey")
    rodape.place(x=135, y=673)


def inputData(window):
    labelsInputData(window)
    balancoInicial(window)
    interestRate(window)
    interestRateOM(window)
    timeYear(window)
    caracteres(window)
    compoundInterval(window)
    depositFunc(window)
    depositFuncOM(window)
    withdrawFuncOM(window)
    withdrawFunc(window)


def balancoInicial(window):
    balancoInicial = Entry(window, width=30)
    balancoInicial.place(x=15, y=107)
    balancoInicialLabel = Label(
        window, text="Balanço Inicial", font=fontConfig(12), bg="lightgrey")
    balancoInicialLabel.place(x=14, y=78)



def interestRate(window):
    interestRate = Entry(window, width=10)
    interestRate.place(x=15, y=162)
    interestRateLabel = Label(
        window, text="Interest Rate", font=fontConfig(12), bg="lightgrey")
    interestRateLabel.place(x=14, y=133)


def interestRateOM(window):
    clickedIR = StringVar()
    clickedIR.set("Yearly")

    dropIR = OptionMenu(window, clickedIR,  "Daily",
                        "Weekly", "Monthly", "Yearly")
    dropIR.place(x=150, y=155)


def timeYear(window):
    timeYear = Entry(window, width=10)
    timeYear.place(x=15, y=217)
    timeYearLabel = Label(
        window, text="Tempo (Anos)", font=fontConfig(12), bg="lightgrey")
    timeYearLabel.place(x=14, y=188)


def caracteres(window):
    moedaLabel1 = Label(
        window, text="€", font=fontConfig(12), bg="lightgrey")
    moedaLabel1.place(x=205, y=100)
    moedaLabel2 = Label(
        window, text="€", font=fontConfig(12), bg="lightgrey")
    moedaLabel2.place(x=205, y=332)
    moedaLabel3 = Label(
        window, text="€", font=fontConfig(12), bg="lightgrey")
    moedaLabel3.place(x=205, y=392)
    percetagemLabel = Label(
        window, text="%", font=fontConfig(12), bg="lightgrey")
    percetagemLabel.place(x=85, y=158)


def compoundInterval(window):
    clickedCI = StringVar()
    clickedCI.set("Monthly")

    dropCI = OptionMenu(window, clickedCI,  "Daily", "Weekly", "Bi-Weekly", "Monthly",
                        "Bi-Monthly", "Quarterly",  "Half-Yearly", "Yearly")
    dropCI.place(x=15, y=272)

    compoundIntervalLabel = Label(
        window, text="Compound interval", font=fontConfig(12), bg="lightgrey")
    compoundIntervalLabel.place(x=14, y=245)


def labelsInputData(window):

    finalTotalLabel = Label(
        window, text="Valor Final", font=fontConfig(20), bg="lightgrey")
    finalTotalLabel.place(x=14, y=430)
    finalTotalLabel = Label(
        window, text="1800000000.2000€", font=fontConfig(20), bg="white", fg="blue")
    finalTotalLabel.place(x=14, y=480)
    finalTotalIRLabel = Label(
        window, text="Interest Rate", font=fontConfig(20), bg="lightgrey")
    finalTotalIRLabel.place(x=14, y=540)
    finalTotalIRLabel = Label(
        window, text="1800000000.2000€", font=fontConfig(20), bg="white", fg="darkorange")
    finalTotalIRLabel.place(x=14, y=590)


def depositFuncOM(window):
    clickedDeposit = StringVar()
    clickedDeposit.set("Monthly")

    dropDeposit = OptionMenu(window, clickedDeposit,
                             "Monthly", "Quarterly",  "Half-Yearly",  "Yearly")
    dropDeposit.place(x=240, y=330)


def depositFunc(window):
    deposit = Entry(window, width=30)
    deposit.place(x=15, y=337)

    depositLabelLabel = Label(
        window, text="Depositar", font=fontConfig(12), bg="lightgrey")
    depositLabelLabel.place(x=14, y=308)


def withdrawFuncOM(window):
    clickedWithdraw = StringVar()
    clickedWithdraw.set("Monthly")

    dropWithdraw = OptionMenu(window, clickedWithdraw,
                              "Monthly", "Quarterly",  "Half-Yearly",  "Yearly")
    dropWithdraw.place(x=240, y=390)


def withdrawFunc(window):
    withdraw = Entry(window, width=30)
    withdraw.place(x=15, y=397)
    withdrawLabelLabel = Label(
        window, text="Retirar", font=fontConfig(12), bg="lightgrey")
    withdrawLabelLabel.place(x=14, y=363)


def calcularButton(window):
    butaoCalcular = Button(window, text="Calcular", bd='5',
                           command=lambda: calcular(window))
    butaoCalcular.place(x=315, y=485)


def calcular(window):
    print("Letsgo")

