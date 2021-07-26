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
    k = input("Digite a sua altura: ")
    k = (72.7*k) - 58
    print("O seu peso ideal é: "+str(k))


def ex13():
    k = float(input("Digite a sua altura: "))
    k1 = (72.7*k) - 58
    k2 = (62.1*k) - 44.7
    print("O seu peso ideal é:\nHomem: "+str(k1)+"kg\nMulher: "+str(k2)+"kg")


def ex14():
    z = 0
    peso = float(input("Digite o peso do peixe: "))
    if (peso > 50):
        price = 4*(int(peso-50))
        z = 1
    if(z != 0):
        print("O excendete será taxado com: "+str(price)+"€")
    else:
        print("O peixe está dentro do preço!")


def ex15():
    k = float(input("Quanto voce ganha por hora?: "))
    h = int(input("Quantas horas trabalhaste este mês?: "))
    f = k*h
    print("Salario bruto: "+str(f)+"€")
    print("Imposto de habitação: "+str(f*0.11)+"€")
    print("SNS: " + str(f*0.08)+"€")
    print("Sindicato: " + str(f*0.05)+"€")
    print("Salario Liquido: "+str(f*(1-0.11-0.08-0.05))+"€")


def ex16():
    m = float(input("Quanto metros quadrados são?: "))
    z = m/3
    k = z/18
    if (k > (int(k))):
        k += 1
    print("É preciso " + str(int(k))+" latas de tinta")


def ex17():  # Incompleto, não tenho paciencia
    m = float(input("Quanto metros quadrados são?: "))
    z = m/6
    k1 = z/18
    k2 = z/3.6
    if (k2 > (int(k2))):
        k2 += 1
    price1 = k1*20
    price2 = k2*6
    print("É preciso " + str(int(k1)) +
          " latas de tinta grandes com o custo de: "+str(price1)+"€")
    print("É preciso " + str(int(k2)) +
          " latas de tinta pequenas com o custo de: "+str(price2)+"€")


def ex18():
    sizeFile = int(input("Indique o tamanho do donwload em MB: "))
    speed = int(input("Indique a velocidade da internet em MB/s: "))
    f=sizeFile/speed
    tempo_aux=(int(f/60))
    print("O seu download demorará: "+str(tempo_aux)+" minutos e "+str(f-(tempo_aux*60)))


def main():
    ex18()


main()
