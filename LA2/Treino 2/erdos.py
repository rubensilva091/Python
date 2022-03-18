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
artigos4 = {
}


def erdos(artigos, n):
    p = "Paul Erdos"
    adj = {}
    queue = [p]
    visited = {p}
    erdos_number = 1
    adj[0] = {p}
    adj[erdos_number] = set()
    while(queue):
        flag = 0
        node = queue.pop(0)
        for books, co_autors in artigos.items():
            if node in co_autors:
                for autor in co_autors:
                    if autor not in visited:
                        visited.add(autor)
                        adj[erdos_number].add(autor)
                        queue.append(autor)
                        flag = 1
        if flag:
            erdos_number += 1
            adj[erdos_number] = set()

    final_list = []
    for i in range(n+1):
        if(i < len(adj)):
            for autor1 in sorted(adj[i]):
                final_list.append(autor1)
    return final_list


print(erdos(artigos4, 4))

#self.assertEqual(erdos(artigos,2),['Paul Erdos', 'Nati Linial', 'Ron Aharoni', 'Benny Sudakov', 'Eli Gafni', 'Uriel Feige', 'Yakov Babichenko', 'Yehuda Afek'])
#self.assertEqual(erdos(artigos,1),['Paul Erdos', 'Nati Linial', 'Ron Aharoni'])
