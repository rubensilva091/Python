'''
Neste problem pretende-se que defina uma função que, dada uma string com palavras, 
devolva uma lista com as palavras nela contidas ordenada por ordem de frequência,
da mais alta para a mais baixa. Palavras com a mesma frequência devem ser listadas 
por ordem alfabética.
'''

texto1 ="o tempo perguntou ao tempo quanto tempo o tempo tem"
texto2 = "ola"


def frequencia(texto):
    lista = texto.split()
    dict_word= {}
    for word in lista:
        n=lista.count(word)
        dict_word.update({word:n})
    dict_word = {k: v for (k, v) in sorted(dict_word.items())}                    #ordernar por key
    dict_word = {k: v for k, v in sorted(dict_word.items(), key=lambda x: -x[1])} #ordenar por value
    final = [x for (x,y) in dict_word.items()]
    print(final)
    return final


frequencia(texto1)
#def test_frequencia_1(self):
#        with test_timeout(self,1):
#            self.assertEqual(frequencia("o tempo perguntou ao tempo quanto tempo o tempo tem"),['tempo','o','ao','perguntou','quanto','tem'])
#
#def test_frequencia_2(self):
#        with test_timeout(self,1):
#            self.assertEqual(frequencia("ola"),['ola'])