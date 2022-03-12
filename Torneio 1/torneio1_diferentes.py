"""

Defina uma função que, dada uma lista de strings, retorne
essa lista ordenada por ordem decrescente do número de 
caracteres diferentes nela contidos.
Caso duas strings tenham o mesmo número de caracteres
diferentes a mais pequena em ordem lexicográfica deve
aparecer primeiro na lista retornada.

"""


frases1 = ["olamundo", "cienciasdacomputacao", "pyhtonefixe"]
frases2 = ["abcdef", "ghijkl", "fedcba", "acebdf"]

#esta javardo, SIUUUUUUUU
def diferentes(frases):
    lista_final = []
    for palavra in frases:
        lista_letras_usadas = []
        for letra in palavra:
            if letra not in lista_letras_usadas:
                lista_letras_usadas.append(letra)
        lista_final.append((palavra, len(lista_letras_usadas)))
    lista_final = sorted(lista_final, key=lambda i: (-i[1], i[0]))
    lista_final= [palavra for palavra,numero in lista_final]
    return lista_final


print(diferentes(frases1))
#self.assertEqual(diferentes(frases),['cienciasdacomputacao', 'pyhtonefixe', 'olamundo'])
#self.assertEqual(diferentes(frases),['abcdef', 'acebdf', 'fedcba', 'ghijkl'])
