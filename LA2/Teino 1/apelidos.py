
'''
Defina uma função que, dada uma lista de nomes de pessoas, devolva essa lista ordenada 
por ordem crescente do número de apelidos (todos menos o primeiro nome). No caso de pessoas com o mesmo número de apelidos,
devem ser listadas por ordem lexicográfica do nome completo.
'''


nomes1 = ['Jose Carlos Bacelar Almeida', 'Maria Joao Frade', 'Jose Bernardo Barros', 'Jorge Manuel Matos Sousa Pinto', 'Manuel Alcino Pereira Cunha', 'Xico Esperto']
nomes2 = ['Pedro Silva','Pedro Pereira']


def apelidos(nomes):
    lista_nr_apelidos = sorted([((len(name.split())-1),name) for name in nomes])
    aux1_list= []
    final_list=[]
    for (size1,name1) in lista_nr_apelidos:
        aux2_list=[]
        for (size2,name2) in lista_nr_apelidos:
            if (size1==size2):
                aux2_list.append(name2)
        if (aux2_list not in aux1_list):
            aux1_list.append(aux2_list)
    for lista in aux1_list:
        sorted(lista)
        for membro in lista:
            final_list.append(membro)
    return final_list

print(apelidos(nomes2))

#
#def test_apelidos_1(self):
#      with test_timeout(self,1):
#      self.assertEqual(apelidos(['Jose Carlos Bacelar Almeida', 'Maria Joao Frade', 'Jose Bernardo Barros', 'Jorge Manuel Matos Sousa Pinto', 'Manuel Alcino Pereira Cunha', 'Xico Esperto']),['Xico Esperto', 'Jose Bernardo Barros', 'Maria Joao Frade', 'Jose Carlos Bacelar Almeida', 'Manuel Alcino Pereira Cunha', 'Jorge Manuel Matos Sousa Pinto'])
#
#def test_apelidos_2(self):
#      with test_timeout(self,1):
#         self.assertEqual(apelidos(['Pedro Silva','Pedro Pereira']),['Pedro Pereira','Pedro Silva'])       