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
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    adj = {}
    queue = [p]
    vis = {p}
    pai = {}
    while(queue):
        # Aceder à stack e extrair a primeira variavel
        v = queue.pop(0)
        if v not in adj:
            adj[v] = set()

        # Adicionar as edges à variavel
        for m in moves:
            if(v[1]+m[1] >= 0 and v[1]+m[1] < len(mapa) and v[0]+m[0] >= 0 and v[0]+m[0] < len(mapa[0])):
                if (mapa[v[1]+m[1]][v[0]+m[0]] != "*"):
                    adj[v].add((v[0]+m[0], v[1]+m[1]))

        # Percorrer todas as Edges da variavel
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                pai[d] = v
                queue.append(d)

    #Area+1 pois a origem nao esta a ser contabilizada inicialmente
    return len(pai)+1

# self.assertEqual(area((3,2),mapa1),5)
# self.assertEqual(area((3,2),mapa2),12)
