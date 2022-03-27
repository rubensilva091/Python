'''
Implemente uma função que calcula o preço mais barato para fazer uma viagem de
autocarro entre duas cidades. A função recebe (para além das duas cidades) uma
lista de rotas de autocarro, onde cada rota é uma sequência de cidades por onde
passa o autocarro, intercalada com o custo para viajar entre cada par de cidades.
Assuma que cada rota funciona nos dois sentidos.
'''

rotas1 = [["Porto", 20, "Lisboa"],
          ["Braga", 3, "Barcelos", 4, "Viana", 3, "Caminha"],
          ["Braga", 3, "Famalicao", 3, "Porto"],
          ["Viana", 4, "Povoa", 3, "Porto"],
          ["Lisboa", 10, "Evora", 8, "Beja", 8, "Faro"]
          ]


rotas2 = [["Porto", 20, "Lisboa"],
          ["Braga", 3, "Barcelos", 4, "Viana", 3, "Caminha"],
          ["Braga", 3, "Famalicao", 3, "Porto"],
          ["Viana", 4, "Povoa", 3, "Porto"],
          ["Lisboa", 10, "Evora", 8, "Beja", 8, "Faro"],
          ["Porto", 15, "Lisboa", 20, "Faro"],
          ["Zelem", 10, "Persetburgs"]
          ]

rotas3 = []


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


def viagem1(rotas, o, d):
    adj = {}
    for rota in rotas:
        for i in range(len(rota)-2):
            if(i % 2 == 0):
                if rota[i] not in adj:
                    adj[rota[i]] = {}
                if rota[i+2] not in adj:
                    adj[rota[i+2]] = {}

                adj[rota[i]][rota[i+2]] = rota[i+1]
                adj[rota[i+2]][rota[i]] = rota[i+1]

    path = floyd_warshall(adj)
    if len(path) < 1:
        return 0
    return path[o][d]

# ____________________________________________________________________________________


def viagem2(rotas, o, dest):
    adj = {}
    pai = {}
    dist = {}
    dist[o] = 0
    orla = {o}
    while orla:
        v = min(orla, key=lambda x: dist[x])
        orla.remove(v)

        if v not in adj:
            adj[v] = {}

        for rota in rotas:
            if v in rota:
                for i in range(len(rota)):
                    if (rota[i] == v):
                        if (i-2 >= 0):
                            adj[v][rota[i-2]] = rota[i-1]
                        if (i+2 < len(rota)):
                            adj[v][rota[i+2]] = rota[i+1]

        # Percorrer as edges
        for d in adj[v]:
            if d not in dist:
                orla.add(d)
                dist[d] = float("inf")
            if dist[v] + adj[v][d] < dist[d]:
                pai[d] = v
                dist[d] = dist[v] + adj[v][d]
            if d == dest:
                orla = {}
                break
    if dest not in dist:
        return 0
    return dist[dest]
