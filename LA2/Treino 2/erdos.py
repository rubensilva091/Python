'''
O número de Erdos é uma homenagem ao matemático húngaro Paul Erdos,
que durante a sua vida escreveu cerca de 1500 artigos, grande parte deles em 
pareceria com outros autores.
O número de Erdos de Paul Erdos é 0. 

Para qualquer outro autor, o seu número de Erdos é igual ao menor 
número de Erdos de todos os seus co-autores mais 1. Dado um dicionário que
associa artigos aos respectivos autores, implemente uma função que
calcula uma lista com os autores com número de Erdos menores que um determinado 
valor. A lista de resultado deve ser ordenada pelo número de Erdos, e, para
autores com o mesmo número, lexicograficamente.
'''

artigos1 = {"Adaptive register allocation with a linear number of registers": {"Carole Delporte-Gallet", "Hugues Fauconnier", "Eli Gafni", "Leslie Lamport"},
            "Oblivious collaboration": {"Yehuda Afek", "Yakov Babichenko", "Uriel Feige", "Eli Gafni", "Nati Linial", "Benny Sudakov"},
            "Optima of dual integer linear programs": {"Ron Aharoni", "Paul Erdos", "Nati Linial"}
            }

artigos2 = {"Specifying systems": {"Leslie Lamport"},
            "Optima of dual integer linear programs": {"Ron Aharoni", "Paul Erdos", "Nati Linial"}
            }


def erdos(artigos, n):
    # Criar o Grafo
    o = "Paul Erdos"
    adj = {}
    queue = [o]
    vis = {o}
    pai = {o: 0}
    while(queue):
        v = queue.pop(0)
        if v not in adj:
            adj[v] = set()

        # Criar as edges de cada escritor
        for key, value in artigos.items():
            if v in value:
                for writer in value:
                    adj[v].add(writer)

        # Percorrer as edges
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                pai[d] = pai[v]+1
                queue.append(d)
    
    #Criar a lista final
    final = [k1 for k1, v1 in sorted(pai.items(), key=lambda i:(i[1], i[0])) if v1 <=n]
    return final

#self.assertEqual(erdos(artigos,2),['Paul Erdos', 'Nati Linial', 'Ron Aharoni', 'Benny Sudakov', 'Eli Gafni', 'Uriel Feige', 'Yakov Babichenko', 'Yehuda Afek'])
#self.assertEqual(erdos(artigos,1),['Paul Erdos', 'Nati Linial', 'Ron Aharoni'])
