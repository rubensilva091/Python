'''
Implemente uma função que calcula a área de um mapa que é acessível por
um robot a partir de um determinado ponto.
O mapa é quadrado e representado por uma lista de strings, onde um '.' representa
um espaço vazio e um '*' um obstáculo.
O ponto inicial consistirá nas coordenadas horizontal e vertical, medidas a 
partir do canto superior esquerdo.
O robot só consegue movimentar-se na horizontal ou na vertical. 
'''

mapa1 = ["..*..",
         ".*.*.",
         "*...*",
         ".*.*.",
         "..*.."]


mapa2 = ["..*..",
         ".*.*.",
         "*....",
         ".*.*.",
         "..*.."]

mapa3 = ["..", ".."]


def area(p, mapa):
    if (p[0] <0 or p[1]<0):
        return 0
    # obter as variaveis iniciais para construir o grafo
    x, y = len(mapa[0]), len(mapa)
    grafo_mapa = {}
    # construir o grafo
    for i in range(y):
        for t in range(x):
            if (t, i) not in grafo_mapa.items():
                grafo_mapa[(t, i)] = set()
            if(t+1 < x):
                if (mapa[i][t+1] != "*"):
                    grafo_mapa[(t, i)].add((t+1, i))
            if(t-1 >= 0):
                if (mapa[i][t-1] != "*"):
                    grafo_mapa[(t, i)].add((t-1, i))
            if(i+1 < y):
                if (mapa[i+1][t] != "*"):
                    grafo_mapa[(t, i)].add((t, i+1))
            if(i-1 >= 0):
                if (mapa[i-1][t] != "*"):
                    grafo_mapa[(t, i)].add((t, i-1))
    # BFS
    queue = [p]
    visited = {p}
    path = {}
    path[p] = p
    while(queue):
        node = queue.pop(0)
        for new_node in grafo_mapa[node]:
            if new_node not in visited:
                visited.add(new_node)
                path[new_node] = node
                queue.append(new_node)
    return len(path)


print(area((3, 2), mapa2))


# self.assertEqual(area((3,2),mapa1),5)
# self.assertEqual(area((3,2),mapa2),12)
