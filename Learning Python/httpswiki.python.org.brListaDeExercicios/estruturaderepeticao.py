import math


def ex1():
    i = 0
    while (i >= 0 and i <= 20):
        i = int(input("Digite aqui a sua nota: "))


def ex2():
    k = input("Digite o seu nome de utilizador: ")
    password = input("Digite a sua password: ")
    while(password == k):
        password = input("PASSWORD ERRADA!!!!!\nDigite novamente: ")


def ex3():
    list = []
    k = input("Digite aqui o seu nome: ")
    while (len(k) <= 3):
        k = input("NOME MUITO PEQUENO\nDigite aqui o seu nome: ")
    list.append("Nome: "+k)
    k = int(input("Digite aqui a sua idade: "))
    while (k < 0 or k > 150):
        k = int(input("IDADE IMPOSSIVEL\nDigite aqui a sua idade: "))
    list.append("Idade: " + str(k))
    k = input("Digite aqui o seu salário: ")
    while (int(k) < 0):
        k = input("SALÁRIO NÃO PODE SER NEGATIVO\nDigite aqui o seu salário: ")
    list.append("Salario: "+str(k))
    k = input("Digite aqui o seu sexo (f/m): ")
    while (k != "f" and k != "m"):
        k = input("IMPOSSIVEL\nDigite aqui o seu sexo (f/m): ")
    list.append("Sexo: "+k)
    k = input("Digite aqui o seu estado civil (s/c/v/d): ")
    while (k != "s" and k != "c" and k != "v" and k != "d"):
        k = input("IMPOSSIVEL\nDigite aqui o seu estado civil (s/c/v/d): ")
    list.append("Estado civil: "+k)
    print(list)


def ex4():
    k1 = 80000
    k2 = 200000
    counter = 0
    while (k1 < k2):
        k1 = k1*1.03
        k2 = k2*1.015
        counter += 1
    print("São precisos "+str(counter)+" anos")


def ex5():
    k1 = (int(input("Digite a população do pais 1: ")))
    t1 = (float(input("Digite a taxa de crescimento do pais 1: ")))
    k2 = (int(input("Digite a população do pais 2: ")))
    t2 = (float(input("Digite a taxa de crescimento do pais 2: ")))
    if (k2 < k1):
        aux1 = k2
        k2 = k1
        k1 = aux1
        aux2 = t2
        t2 = t1
        t1 = aux2
    counter = 0
    while (k1 < k2):
        k1 = k1*(1+t1/100)
        k2 = k2*(1+t2/100)
        counter += 1
    print("São precisos "+str(counter)+" anos")


def ex6():
    string = ""
    for i in range(1, 21):
        print(i)
    for i in range(1, 21):
        string = string + str(i) + " "
    print("\n\n" + string)


def ex7():
    j = 0
    for i in range(5):
        k = (int(input("Digite o numero "+str(i+1)+" : ")))
        if (j < k):
            j = k
    print("O maior numero foi: " + str(j))


def ex8():
    j = 0
    m = 0
    for i in range(5):
        k = (int(input("Digite o numero "+str(i+1)+" : ")))
        j = j+k
    m = j/5
    print("A soma dos numeros é: " + str(j)+"\nA media dos numeros é: "+str(m))


def ex9():
    string = ""
    for i in range(1, 51):
        if (i % 2 != 0):
            string = string + str(i) + " "
    print(string)


def ex10():
    k1 = int(input("Digite o numero inteiro 1: "))
    k2 = int(input("Digite o numero inteiro 2: "))
    string = ""
    if(k2 < k1):
        aux = k1
        k1 = k2
        k2 = aux
    for i in range(k1+1, k2):
        string = string + str(i) + " "
    print(string)


def ex11():
    k1 = int(input("Digite o numero inteiro 1: "))
    k2 = int(input("Digite o numero inteiro 2: "))
    k=0
    if(k2 < k1):
        aux = k1
        k1 = k2
        k2 = aux
    for i in range(k1+1, k2):
        k=k+i
    print("O resultado da soma dos numeros entre o primeiro e o segundo é: "+str(k))


def main():
    ex11()


main()
