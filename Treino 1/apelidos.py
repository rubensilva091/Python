
'''
Defina uma função que, dada uma lista de nomes de pessoas, devolva essa lista ordenada 
por ordem crescente do número de apelidos (todos menos o primeiro nome). No caso de pessoas com o mesmo número de apelidos,
devem ser listadas por ordem lexicográfica do nome completo.
'''

nomes1 = ['Jose Carlos Bacelar Almeida', 'Maria Joao Frade', 'Jose Bernardo Barros', 'Jorge Manuel Matos Sousa Pinto', 'Manuel Alcino Pereira Cunha', 'Xico Esperto']
nomes2 = ['Pedro Silva','Pedro Pereira', 'pedro']


def apelidos(nomes):
    apelidos = {}

    #Contar o numero de apelidos e criar um dict
    for n in nomes:
        apelidos[n] = len(n.split())-1

    #Criar a lista final pelo dict ordenado
    lista_final= [name for (name, n) in sorted(apelidos.items(), key=lambda i: (i[1], i[0]))]

    return lista_final


#self.assertEqual(apelidos(['Jose Carlos Bacelar Almeida', 'Maria Joao Frade', 'Jose Bernardo Barros', 'Jorge Manuel Matos Sousa Pinto', 'Manuel Alcino Pereira Cunha', 'Xico Esperto']),['Xico Esperto', 'Jose Bernardo Barros', 'Maria Joao Frade', 'Jose Carlos Bacelar Almeida', 'Manuel Alcino Pereira Cunha', 'Jorge Manuel Matos Sousa Pinto'])
#self.assertEqual(apelidos(['Pedro Silva','Pedro Pereira']),['Pedro Pereira','Pedro Silva'])       