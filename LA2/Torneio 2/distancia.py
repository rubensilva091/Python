'''

Neste problema pretende-se que implemente uma função que calcula a distância
entre duas cidades num mapa.

O mapa é rectangular e definido por uma lista de strings de igual comprimento,
onde um caracter 'X' marca a existência de uma cidade e um '#' uma estrada.
Neste mapa só é possível viajar na horizontal ou na vertical. As cidades de
origem e destino são identificadas pelas respectivas coordenadas horizontal e
vertical, medidas a partir do canto superior esquerdo. 

#!
Se as coordenadas destino e origem não forem cidades a função deverá retornar None. 
Se não houver caminho entre as duas cidades deverá retornar float("inf").

'''


mapa1 = ["#X###X",
         "#  #  ",
         "#X##  ",
         "     X",
         "  X###"]


def caminho(pai, o, d):
    caminho = [d]
    while d in pai:
        d = pai[d]
        caminho.insert(0, d)
    return caminho


def distancia(mapa, o, d):
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    adj = {}
    pai = {}
    vis = {o}
    queue = [o]
    while queue:
        v = queue.pop(0)
        if v not in adj:
            adj[v] = set()

        for m in moves:
            new_X = v[0]+m[0]
            new_Y = v[1]+m[1]
            if new_X >= 0 and new_X < len(mapa[0]) and new_Y >= 0 and new_Y < len(mapa):
                if (mapa[new_Y][new_X] == "#" or mapa[new_Y][new_X] == "X"):
                    adj[v].add((new_X, new_Y))

        for node in adj[v]:
            if node not in vis:
                vis.add(node)
                pai[node] = v
                queue.append(node)
            if node == d:
                queue = []
                break
    pai = caminho(pai, o, d)

    # Returns
    if (mapa[o[1]][o[0]] != "X" or mapa[d[1]][d[0]] != "X"):
        return None
    if (len(pai)-1) == 0:
        return float("inf")
    return len(pai)-1


print(distancia(mapa1, (1, 0), (1, 2)))
#self.assertEqual(distancia(mapa1,(1,0),(1,2)), 4)
#self.assertEqual(distancia(mapa2,(1,0),(1,1)), None)


def bfs(adj, o):
    pai = {}
    vis = {o}
    queue = [o]
    while queue:
        v = queue.pop(0)
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                pai[d] = v
                queue.append(d)
    return pai
