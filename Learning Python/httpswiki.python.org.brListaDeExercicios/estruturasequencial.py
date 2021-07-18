import math


def ex1():
    print("Ola Mundo")


def ex2():
    k = int(input())
    print("O numero mostrado foi: "+str(k))


def ex2_1():
    print("O numero mostrado foi: "+str(int(input())))


def ex3():
    k1, k2 = int(input()), int(input())
    k = k1+k2
    print("O numero mostrado foi: "+str(k))


def ex4():
    print("Digite as 4 notas dos alunos: ")
    k1, k2, k3, k4 = int(input()), int(input()), int(input()), int(input())
    k = (k1+k2+k3+k4)/4
    print("A Media do aluno é: "+str(k))


def ex5():
    k = int(input("Digite o tamanho que deseja em metros: "))
    print(str(k)+" m -> " + str(k*100)+" cm")


def ex6():
    k = int(input("Digite o tamanho do raio do circulo: "))
    k = math.pow(k, 2)
    k = k*math.pi
    print("O circulo tem tamanho: "+str(k) + " unidades")


def ex7():
    k = int(input("Digite o tamanho do lado do quadrado: "))
    k = k*8
    print("O dobro da area do quadrado é: "+str(k)+" unidades")


def ex8():
    k1 = int(input("Quantas horas trabalhas por mes: "))
    k2 = int(input("Quanto é o salário por hora: "))
    k = k1*k2
    print("O salário num mês é: "+str(k)+"€")


def ex9():
    k = float(input("Fahrenheit: "))
    k1 = 5 * ((k-32) / 9)
    print("Fahrenheit: "+str(k)+"  ->  Celsius: " + str(k1))


def ex10():
    k = float(input("Celsius: "))
    k1 = (((k/5)*9)+32)
    print("Celsius: "+str(k)+"  ->  Fahrenheit: " + str(k1))


def ex11():
    k1, k2 = int(input("Inteiro1: ")), int(input("Inteiro2: "))
    k3 = float(input("Float: "))
    a = (k1*2)*(k2/2)
    b = (k1*3) + k3
    c = math.pow(k3, 3)
    print("a -> Produto do dobro do primeiro da metade do segundo: "+str(a) +
          "\nb -> A soma do triplo do primeiro com o terceiro: "+str(b)+"\nb -> O terceiro elevado ao cubo: "+str(c))

def ex12():
    

def main():
    ex11()


main()
