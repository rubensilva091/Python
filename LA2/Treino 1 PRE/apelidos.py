'''
Defina uma função que, dada uma lista de nomes de pessoas, devolva essa lista ordenada 
por ordem crescente do número de apelidos (todos menos o primeiro nome). No caso de pessoas com o mesmo número de apelidos,
devem ser listadas por ordem lexicográfica do nome completo.
'''


nomes1 = ['Jose Carlos Bacelar Almeida', 'Maria Joao Frade', 'Jose Bernardo Barros', 'Jorge Manuel Matos Sousa Pinto', 'Manuel Alcino Pereira Cunha', 'Xico Esperto']
nomes2 = ['Pedro Silva','Pedro Pereira']


def apelidos(nomes):
    dict_nome = {}
    for nome in nomes:
        quantidade_de_apelidos = len(nome.split()) - 1
        dict_aux = {nome:quantidade_de_apelidos}
        dict_nome.update(dict_aux)
    dict_nome = {k: v for (k,v) in sorted(dict_nome.items(),key=lambda x:(-x[1],x[0]))}    #primeira ordenação por lexical
    dict_nome = {k: v for (k, v) in sorted(dict_nome.items(), key=lambda item: item[1])}   #segunda ordenação por value
    final = []
    for (x,y) in dict_nome.items():
        final.append(x)
    return final

#Thoughts finais, em vez de usar dicionario, poderia ter usado listas com duplos, sou estupido O.o

apelidos(nomes1)
        
#
#def test_apelidos_1(self):
#      with test_timeout(self,1):
#      self.assertEqual(apelidos(['Jose Carlos Bacelar Almeida', 'Maria Joao Frade', 'Jose Bernardo Barros', 'Jorge Manuel Matos Sousa Pinto', 'Manuel Alcino Pereira Cunha', 'Xico Esperto']),['Xico Esperto', 'Jose Bernardo Barros', 'Maria Joao Frade', 'Jose Carlos Bacelar Almeida', 'Manuel Alcino Pereira Cunha', 'Jorge Manuel Matos Sousa Pinto'])
#
#def test_apelidos_2(self):
#      with test_timeout(self,1):
#         self.assertEqual(apelidos(['Pedro Silva','Pedro Pereira']),['Pedro Pereira','Pedro Silva'])       