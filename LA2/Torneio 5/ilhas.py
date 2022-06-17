'''

Neste problema pretende-se que implemente uma função que calcula quantas
ilhas existem num mapa.

O mapa é rectangular e definido por uma lista de strings de igual comprimento,
onde um caracter '#' marca uma quadrícula com terra e um ' ' uma quadrícula com
mar. A função deve devolver o n´úmero de ilhas no mapa.

'''




mapa1 = ["## ###",
         "## #  ",
         "#  #  ",
         "      ",
         "   ###"]

mapa5 = ["##    ",
         "## #  ",
         "#  #  ",
         " ##   ",
         "   # #"]

mapa2 = ["## ###",
         "####  ",
         "#  #  ",
         "###   ",
         "   ###"]
mapa3 = ["###",
         "# #",
         "###"]

mapa4 = ["   ",
         "   ",
         "   "]


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

    if len(pai.keys()) == 0 or len(pai.values()) == 0:
        return 0
    return min(min(pai.keys()), min(pai.values()))


def ilhas(mapa):
    # obter as variaveis iniciais para construir o grafo
    x, y = len(mapa[0]), len(mapa)
    grafo_mapa = {}
    # construir o grafo
    for i in range(y):
        for t in range(x):
            if (t, i) not in grafo_mapa.items() and mapa[i][t] != " ":
                grafo_mapa[(t, i)] = set()
            if(t+1 < x):
                if (mapa[i][t+1] != " " and mapa[i][t] != " "):
                    grafo_mapa[(t, i)].add((t+1, i))
            if(t-1 >= 0):
                if (mapa[i][t-1] != " " and mapa[i][t] != " "):
                    grafo_mapa[(t, i)].add((t-1, i))
            if(i+1 < y):
                if (mapa[i+1][t] != " " and mapa[i][t] != " "):
                    grafo_mapa[(t, i)].add((t, i+1))
            if(i-1 >= 0):
                if (mapa[i-1][t] != " " and mapa[i][t] != " "):
                    grafo_mapa[(t, i)].add((t, i-1))

    print(grafo_mapa)
    list = []
    for i in range(y):
        for t in range(x):
            if (mapa[i][t] != " "):
                var = bfs(grafo_mapa, (t, i))
                if(var == 0):
                    list.append(var)
                if var not in list and var != 0:
                    list.append(var)
    return len(list)


print(ilhas(mapa5))

# mapa = ["## ###",
#        "## #  ",
#        "#  #  ",
#        "      ",
#        "   ###"]
# self.assertEqual(ilhas(mapa), 3)
# mapa = ["## ###",
#        "####  ",
#        "#  #  ",
#        "###   ",
#        "   ###"]
# self.assertEqual(ilhas(mapa), 2)
