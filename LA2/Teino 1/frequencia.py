'''
Neste problem pretende-se que defina uma função que, dada uma string com palavras, 
devolva uma lista com as palavras nela contidas ordenada por ordem de frequência,
da mais alta para a mais baixa. Palavras com a mesma frequência devem ser listadas 
por ordem alfabética.
'''


texto1 = "o tempo perguntou ao tempo quanto tempo o tempo tem"
texto2= "ola"


def frequencia(texto):
    new_texto = texto.split()
    aux_texto = []
    final_texto=[]
    for word1 in new_texto:
            counter=0
            for word2 in new_texto:
                if (word1==word2):
                    counter+=1
            aux_texto.append((counter,word1))
    aux_texto = sorted(aux_texto, reverse=True)
    for k,v in aux_texto:
        if (v not in final_texto):
            final_texto.append(v)
    return final_texto

print(frequencia(texto1))



#   def test_frequencia_1(self):
#       with test_timeout(self,1):
#           self.assertEqual(frequencia("o tempo perguntou ao tempo quanto tempo o tempo tem"),['tempo','o','ao','perguntou','quanto','tem'])#

#   def test_frequencia_2(self):
#       with test_timeout(self,1):
#           self.assertEqual(frequencia("ola"),['ola'])