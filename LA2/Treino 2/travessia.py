'''
Implemente uma função que calcula o menor custo de atravessar uma região de
Norte para Sul. O mapa da região é rectangular, dado por uma lista de strings,
onde cada digito representa a altura de cada ponto. Só é possível efectuar 
movimentos na horizontal ou na vertical, e só é possível passar de um ponto
para outro se a diferença de alturas for inferior ou igual a 2, sendo o custo 
desse movimento 1 mais a diferença de alturas. O ponto de partida (na linha
mais a Norte) e o ponto de chegada (na linha mais a Sul) não estão fixados à
partida, devendo a função devolver a coordenada horizontal do melhor
ponto para iniciar a travessia e o respectivo custo. No caso de haver dois pontos
com igual custo, deve devolver a coordenada mais a Oeste.
'''

mapa1 = ["4563",
         "9254",
         "7234",
         "3231",
         "3881"]

mapa2 = ["90999",
         "00000",
         "92909",
         "94909"]

mapa3 = ["000",
         "888",
         "111"]



def floyd_warshall(adj):
    dist = {}
    for o in adj:
        dist[o] = {}
        for d in adj:
            if o == d:
                dist[o][d] = 0
            elif d in adj[o]:
                dist[o][d] = adj[o][d]
            else:
                dist[o][d] = float("inf")
    for k in adj:
        for o in adj:
            for d in adj:
                if dist[o][k] + dist[k][d] < dist[o][d]:
                    dist[o][d] = dist[o][k] + dist[k][d]
    return dist


def travessia(mapa):
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    adj = {}

    # Obter o grafo
    for y in range(len(mapa)):
        for x in range(len(mapa[0])):
            if (x, y) not in adj:
                adj[(x, y)] = {}

            # tdo o calculo necessario para o grafo
            for m in moves:
                if(x+m[0] >= 0 and x+m[0] < len(mapa[0]) and y+m[1] >= 0 and y+m[1] < len(mapa)):
                    new_n = abs(int(mapa[y][x])-int(mapa[y+m[1]][x+m[0]]))
                    if(new_n <= 2):
                        adj[(x, y)][(x+m[0], y+m[1])] = new_n + 1

    final = []
    r = 9999999
    path = floyd_warshall(adj)
    size = len(mapa[0])

    # COMO PERCORRER O OUTPUT DO FLOYD WARSHELL
    for origem in range(size):
        for destino in range(size):
            if path[(origem, 0)][(destino, y)] <= r:
                r = path[(origem, 0)][(destino, y)]

                o = (origem, r)

                final.append(o)
    final = sorted(final, key=lambda i: (i[1], i[0]))[0]
    return final


print(travessia(mapa1))
# self.assertEqual(travessia(mapa1),(2,10))
# self.assertEqual(travessia(mapa2),(1,5))
