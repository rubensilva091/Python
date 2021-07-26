import math


def ex1():
    k1, k2 = int(input("Digite o numero 1: ")), int(
        input("Digite o numero 2: "))
    if (k1 > k2):
        print("O numero maior é: "+str(k1))
    else:
        print("O numero maior é: "+str(k2))


def ex2():
    k1 = int(input("Digite o numero que deseja testar: "))
    if (k1 > 0):
        print("O numero é positivo!")
    elif(k1 < 0):
        print("O numero é negativo!")
    else:
        print("Neutro")


def ex3():
    k = input("Digite o sexo F ou M: ")
    if (k == "F" or k == "f"):
        print("É Feminino")
    elif (k == "M" or k == "m"):
        print("É Masculino")
    else:
        print("É Trans")


def ex4():
    k = input("Digite a letra: ")
    vogal = ["a", "e", "i", "o", "u"]
    if(k.lower() in vogal):
        print("É vogal!")
    else:
        print("É Consoante!")


def ex5():
    k = float(input("Digite a nota: "))
    if (k < 0 or k > 20):
        print("NAO EXISTE!")
    elif (k <= 9.5):
        print("Reprovado!")
    elif (k > 9.5 and k != 20):
        print("Aprovado")
    elif (k == 20):
        print("Aprovado com distinção")


def ex6():
    k1, k2, k3 = int(input("Digite o numero 1: ")), int(
        input("Digite o numero 2: ")), int(input("Digite o numero 3: "))
    if (k1 > k2 and k1 > k3):
        print("O maior é: "+str(k1))
    elif (k2 > k1 and k2 > k3):
        print("O maior é: "+str(k2))
    else:
        print("O maior é: "+str(k3))


def ex7():

    k1, k2, k3 = int(input("Digite o numero 1: ")), int(
        input("Digite o numero 2: ")), int(input("Digite o numero 3: "))
    if (k1 > k2 and k1 > k3):
        if(k2 > k3):
            print("O maior é: "+str(k1)+"\nO menor é: "+str(k2))
        else:
            print("O maior é: "+str(k3)+"\nO menor é: "+str(k3))
    elif (k2 > k1 and k2 > k3):
        if(k3 > k1):
            print("O maior é: "+str(k2)+"\nO menor é: "+str(k3))
        else:
            print("O maior é: "+str(k2)+"\nO menor é: "+str(k1))
    else:
        if(k2 > k1):
            print("O maior é: "+str(k3)+"\nO menor é: "+str(k1))
        else:
            print("O maior é: "+str(k3)+"\nO menor é: "+str(k2))


#NAO FIZ MAIS!


#def main():
    #ex8()


#main()
