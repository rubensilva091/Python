"""

Um ladrão assalta uma casa e, dado que tem uma capacidade de carga limitada, 
tem que decidir que objectos vai levar por forma a maximizar o potencial lucro. 

Implemente uma função que ajude o ladrão a decidir o que levar.
A função recebe a capacidade de carga do ladrão (em Kg) seguida de uma lista 
dos objectos existentes na casa, sendo cada um um triplo com o nome, o valor de 
venda no mercado negro, e o seu peso. Deve devolver o máximo lucro que o ladrão
poderá  obter para a capacidade de carga especificada.

"""

objectos1 = [("microondas", 30, 6), ("jarra", 14, 3),
             ("giradiscos", 16, 4), ("radio", 9, 2)]
objectos2 = [('A', 10, 1), ('B', 20, 1), ('C', 30, 1), ('D', 40, 1), ('E', 50, 1),
             ('F', 60, 1), ('G', 70, 1), ('H', 80, 1), ('I', 90, 1), ('J', 100, 1)]


# Obtem o maximo de combinaçoes possiveis
def n_length_combo(lst, n):

    if n == 0:
        return [[]]
    l = []
    for i in range(len(lst)):

        m = lst[i]
        remLst = lst[i + 1:]

        for p in n_length_combo(remLst, n-1):
            l.append([m]+p)
    return l


def ladrao(capacidade, objectos):
    i = 1
    flag = 1
    max_price = 0
    while(flag):
        flag = 0
        final = n_length_combo(objectos, i)
        for list1 in final:
            peso = 0
            price = 0
            for list2 in list1:
                price += list2[1]
                peso += list2[2]
            if peso <= capacidade:
                flag = 1
                max_price = max(price, max_price)
        i += 1
    return max_price


print(ladrao(10, objectos2))
# def test_ladrao_1(self):
#     with test_timeout(self,2):
#         objectos = [("microondas",30,6),("jarra",14,3),("giradiscos",16,4),("radio",9,2)]
#         self.assertEqual(ladrao(10,objectos),46)
# def test_ladrao_2(self):
#     with test_timeout(self,2):
#         objectos = [('A',10,1),('B',20,1),('C',30,1),('D',40,1),('E',50,1),('F',60,1),('G',70,1),('H',80,1),('I',90,1),('J',100,1)]
#         self.assertEqual(ladrao(10,objectos),550)
