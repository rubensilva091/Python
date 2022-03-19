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
          ["Porto", 15, "Lisboa", 20, "Faro"]
          ]


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


def viagem(rotas, o, d):
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
    if len(path)<1:
        return 0
    return path[o][d]


print(viagem(rotas2, "Braga", "Faro"))

# self.assertEqual(viagem(rotas1,"Caminha","Lisboa"),30)
# self.assertEqual(viagem(rotas2,"Braga","Faro"),41)
