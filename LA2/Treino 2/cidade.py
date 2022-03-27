'''
Podemos usar um (multi) grafo para representar um mapa de uma cidade:
cada nó representa um cruzamento e cada aresta uma rua.

Pretende-se que implemente uma função que calcula o tamanho de uma cidade,
sendo esse tamanho a distância entre os seus cruzamentos mais afastados.

A entrada consistirá numa lista de nomes de ruas (podendo assumir que os
nomes de ruas são únicos). Os identificadores dos cruzamentos correspondem a
letras do alfabeto, e cada rua começa (e acaba) no cruzamento
identificado pelo primeiro (e último) caracter do respectivo nome.
'''


ruas1 = ["raio", "central", "liberdade", "chaos", "saovictor",
         "saovicente", "saodomingos", "souto", "capelistas", "anjo", "taxa"]

ruas2 = ["ab", "bc", "bd", "cd"]


def dijkstra(adj, o):
    dist = {}
    dist[o] = 0
    orla = {o}
    while orla:
        v = min(orla, key=lambda x: dist[x])
        orla.remove(v)
        for d in adj[v]:
            if d not in dist:
                orla.add(d)
                dist[d] = float("inf")
            if dist[v] + adj[v][d] < dist[d]:
                dist[d] = dist[v] + adj[v][d]
    return dist


def tamanho(ruas):
    adj = {}

    # Criar o grafo
    for r in ruas:
        if r[0] not in adj:
            adj[r[0]] = {}

        if r[-1] not in adj:
            adj[r[-1]] = {}

        # Este passo é extrema importancia, pois cada 2 cruzamentos podem ter diversas arestas, e interessa nos a menor delas
        if r[-1] not in adj[r[0]]:
            adj[r[0]][r[-1]] = 9999999
        if r[0] not in adj[r[-1]]:
            adj[r[-1]][r[0]] = 9999999

        adj[r[0]][r[-1]] = min(len(r), adj[r[0]][r[-1]])
        adj[r[-1]][r[0]] = min(len(r), adj[r[-1]][r[0]])

    # descubrir o maior path
    final = []
    for o in adj:
        path = dijkstra(adj, o)
        aux = 0
        if len(path) > 0:
            aux = sorted(path.items(), key=lambda i: -i[1])[0][1]
        final.append(aux)
    return max(final)

# self.assertEqual(tamanho(ruas1),25)
# self.assertEqual(tamanho(ruas2),4)
