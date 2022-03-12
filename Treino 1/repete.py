'''
Implemente uma função que determine qual a menor sequência de caracters que
contém n repetições de uma determinada palavra
'''


def repete(palavra, n):
    counter = 0

    # Descobrir as sequencias de letras que podem ser eliminadas e contar-las
    for i in range(0, len(palavra)):
        j = len(palavra)-i-1
        if(i >= j):
            break
        if(palavra[i] == palavra[j]):
            counter += 1
        else:
            break

    # Primeiro, juntar todas as strings sem as repitiçoes, e no final adicionar as repetiçoes
    palavra = palavra[:-counter] * n + palavra[:counter]
    return palavra

# self.assertEqual(repete("amanha",2),"amanhamanha")
# self.assertEqual(repete("ola",3),"olaolaola")
