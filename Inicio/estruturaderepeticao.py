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
    k = 0
    if(k2 < k1):
        aux = k1
        k1 = k2
        k2 = aux
    for i in range(k1+1, k2):
        k = k+i
    print("O resultado da soma dos numeros entre o primeiro e o segundo é: "+str(k))


def ex12():
    k1 = int(input("Digite o numero inteiro para a tabuada: "))
    print("\n\n\nTabuada do "+str(k1)+" :\n")
    for i in range(10):
        print(str(i+1)+" x " + str(k1) + " = "+str(k1*(i+1)))


def ex13():
    k1 = int(input("Digite a base: "))
    k2 = int(input("Digite o expoente: "))
    k = 0
    for i in range(k2):
        k = k1*(i+1)
    print("O numero de "+str(k1)+"^"+str(k2)+" é: "+str(k))


def ex14():
    cPar = 0
    cImpar = 0
    for i in range(10):
        k = int(input("Digite o numero "+str(i+1)+" : "))
        if(k % 2 == 0):
            cPar += 1
        else:
            cImpar += 1
    print("Teve "+str(cPar)+" Pares!\nTeve "+str(cImpar)+" Impares!")


def ex15():
    n = int(input("Digite o n-th membro do fibonnaci: "))
    a = 0
    b = 1
    if n < 0:
        print("IMPOSSIVEL")
    elif n == 0:
        print("0")
    elif n == 1:
        print("1")
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
    print("FINAL: "+str(b))


def ex16():
    n = 10000
    a = 0
    b = 1
    k = 0
    if n < 0:
        print("IMPOSSIVEL")
    elif n == 0:
        print("0")
    elif n == 1:
        print("1")
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            if(b <= 500):
                k = b
            else:
                break
    print("FINAL: "+str(k))


def ex17():
    n = int(input("Digite qual numero deseja aplicar o fatorial: "))
    k = 1
    for i in range(1, n+1):
        k = k*i
    print("FINAL: "+str(k))


def ex18():
    n = int(input("Digite qual o tamanho da injecao numerica?: "))
    k = 1
    menor, maior = 999999999, 0
    soma = 0
    for i in range(n):
        k = int(input("Digite o numero "+str(i+1)+" : "))
        if (k < menor):
            menor = k
        if (k > maior):
            maior = k
        soma += k
    print("MAIOR VALOR: "+str(maior)+"\nMENOR VALOR: " +
          str(menor)+"\nSOMA: "+str(soma))


def ex19():
    n = int(input("Digite qual o tamanho da injecao numerica?: "))
    k = 1
    menor, maior = 999999999, 1
    soma = 0
    for i in range(n):
        k = int(input("Digite o numero "+str(i+1)+" : "))
        while (k < 0 or k > 1000):
            k = int(input("NUMERO INVALO\nDIGITE OUTRA VEZ: "+str(i+1)+" : "))
        if (k < menor):
            menor = k
        if (k > maior):
            maior = k
        soma += k
    print("MAIOR VALOR: "+str(maior)+"\nMENOR VALOR: " +
          str(menor)+"\nSOMA: "+str(soma))

# nao percebi este....
# def ex20():

# verif


def ex21(n):
    k = 0
    z = 0
    if (n > 0):
        k = n
    else:
        k = int(input("Digite o numero que deseja verificar se é primo: "))
    for i in range(k):
        if(((k % (i+1)) == 0 and (i+1) != k) and (i+1) != 1):
            z = 1
            print("Não é numero primo")
            return (i+1)
    if (z == 0):
        print("É numero primo!")
        return 0


def ex22():
    x = ex21(0)
    if(x != 0):
        print("Nao foi primo em: "+str(x))


def ex23():
    n = int(input("Digite o numero maximo que deseja procurar primos: "))
    string = ""
    for j in range(1, n):
        k = j
        z = 0
        for i in range(k):
            if(((k % (i+1)) == 0 and (i+1) != k) and (i+1) != 1):
                z = 1
                break
        if (z == 0):
            string = string + " " + str(k)
    print("Este são os numeros primos:"+string)


# Nao entendi nada
# def ex24():

def ex25():
    k, i, somatorio = 1, 0, 0
    while(k > 0):
        i += 1
        k = int(input("Digite a idade da pessoa nr "+str(i)+" : "))
        if(k > 0):
            somatorio = somatorio + k
    final = somatorio/(i-1)
    if (final >= 0 and final <= 25):
        print("A turma é jovem!")
    elif(final > 25 and final <= 60):
        print("A turma é adulta!")
    else:
        print("A turma é idosa!")


def ex26():
    k, i = 1, 0
    ruiben, salomao, gary = 0, 0, 0
    while(k > 0 and k != 4):
        i += 1
        k = int(input(
            "OLA ELEITOR nr "+str(i)+"\nDigite qual o deputado\n1->Ruiben\n2->Salomão\n3->Gary\n4->SAIR\nQUAL: "))
        while (k != 1 and k != 2 and k != 3 and k != 4):
            k = int(input("NUMERO ERRO\nDigite novamente: "))
        if (k == 1):
            ruiben += 1
        if (k == 2):
            salomao += 1
        if (k == 3):
            gary += 1
    print("=====RESULTADO FINAL=====")
    print("\nRUIBEN -> "+str(ruiben))
    print("\nSALOMÃO -> "+str(salomao))
    print("\nGARY -> "+str(gary))
    print("\n")


def ex27():
    turma = int(input("Digite o numero de turmas: "))
    somatorio = 0
    i = 0
    if turma < 0:
        return  # so para evitar dar problemas xD
    for i in range(turma):
        nAlunosTurma = int(
            input("Quantos alunos tem a turma "+str(i+1)+" ?: "))
        while (nAlunosTurma < 0 or nAlunosTurma > 40):
            nAlunosTurma = int(input("ENTRE 0 e 40: "))
        somatorio = somatorio + nAlunosTurma
    somatorio = somatorio/(i+1)
    print("Em media, as turmas teem: "+str(somatorio)+" alunos")


def ex28():
    nCD = int(input("Quandos CDs possui? "))
    somatorio, i = 0, 0
    for i in range(nCD):
        n = int(input("Quanto custou o CD nr "+str(i+1)+(" : ")))
        somatorio = somatorio + n
    somatorio = somatorio/(i+1)
    print("Em media, o colecionador gastou: "+str(somatorio)+"€ ")

def ex29():
    

def main():
    ex28()


main()
