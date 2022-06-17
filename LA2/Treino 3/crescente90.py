"""

Implemente uma função que dada uma sequência de inteiros, determinar o 
comprimento da maior sub-sequência (não necessariamente contígua) que se 
encontra ordenada de forma crescente.

Sugere-se que comece por implementar uma função auxiliar recursiva que determina 
o comprimento da maior sub-sequência crescente que inclui o primeiro elemento
da sequência, sendo o resultado pretendido o máximo obtido aplicando esta
função a todos os sufixos da sequência de entrada.

"""


lista1 = [5, 2, 7, 4, 3, 8]
lista2 = [15, 27, 14, 38, 26, 55, 46, 65, 85]
lista3 = []
lista4=[1]


def crescente(lista):
    if len(lista)==0:
        return 0
    list1=[0]
    for i in range(len(lista)):
        counter = 0
        last_member = lista[i]
        for y in range(i, len(lista)):
            if (lista[y] >= last_member):
                counter += 1
                last_member = lista[y]
        list1.append(counter)
    return max(list1)


print(crescente(lista1))

# def test_crescente_1(self):
#    with test_timeout(self,2):
#        lista = [5,2,7,4,3,8]
#        self.assertEqual(crescente(lista),3)

# def test_crescente_2(self):
#    with test_timeout(self,2):
#        lista = [15,27,14,38,26,55,46,65,85]
#        self.assertEqual(crescente(lista),6)
