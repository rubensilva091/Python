'''
Neste problema pretende-se que defina uma função que, dada uma string com palavras, 
devolva uma lista com as palavras nela contidas ordenada por ordem de frequência,
da mais alta para a mais baixa. Palavras com a mesma frequência devem ser listadas 
por ordem alfabética.
'''


texto1 = "o tempo perguntou ao tempo quanto tempo o tempo tem"
texto2= "ola"


def frequencia(texto):
    palavras = {}

    #contar todas as palavras e colocar no dicionario
    texto = texto.split()
    for n in texto:
        palavras[n]= texto.count(n)

    #criar a lista com as palavras ordenadas
    lista_final = [key for key,value in sorted(palavras.items(), key=lambda i: (-i[1],i[0]))]
    return lista_final


#self.assertEqual(frequencia("o tempo perguntou ao tempo quanto tempo o tempo tem"),['tempo','o','ao','perguntou','quanto','tem'])#
#self.assertEqual(frequencia("ola"),['ola'])