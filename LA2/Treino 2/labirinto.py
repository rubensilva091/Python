'''
Implemente uma função que calcula um dos caminhos mais curtos para atravessar
um labirinto. O mapa do labirinto é quadrado e representado por uma lista 
de strings, onde um ' ' representa um espaço vazio e um '#' um obstáculo.
O ponto de entrada é o canto superior esquerdo e o ponto de saída o canto
inferior direito. A função deve devolver uma string com as instruções para
atravesar o labirinto. As instruções podem ser 'N','S','E','O'.
'''

mapa1 = ["  ########",
         "# # #    #",
         "# # #### #",
         "# #      #",
         "# # # ####",
         "# # #    #",
         "#   # #  #",
         "##### ####",
         "#        #",
         "########  "]

mapa2 = ['   ',
         ' # ',
         '   ']


def caminho(mapa):
    o = (0, 0)
    adj = {}
    queue = [o]
    vis = {o}
    pai = {}
    while(queue):
        v = queue.pop(0)
        if v not in adj:
            adj[v] = set()

        # Criar o path finder
        # mapa [y][x] por primeiro ves os indexs, e so dps as strings
        if (v[0]+1 >= 0 and v[0]+1 < len(mapa[0]) and mapa[v[1]][v[0]+1] != "#"):
            adj[v].add((v[0]+1, v[1]))
        if (v[1]+1 >= 0 and v[1]+1 < len(mapa) and mapa[v[1]+1][v[0]] != "#"):
            adj[v].add((v[0], v[1]+1))
        if (v[0]-1 >= 0 and v[0]-1 < len(mapa[0]) and mapa[v[1]][v[0]-1] != "#"):
            adj[v].add((v[0]-1, v[1]))
        if (v[1]-1 >= 0 and v[1]-1 < len(mapa) and mapa[v[1]-1][v[0]] != "#"):
            adj[v].add((v[0], v[1]-1))
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                pai[d] = v
                queue.append(d)

    # Shortest Path
    d = (len(mapa)-1, len(mapa[0])-1)
    caminho = [d]
    while d in pai:
        d = pai[d]
        caminho.insert(0, d)

    # Passar de Coordenadas para Comandos
    final = ""
    for i in range(len(caminho)-1):
        aux = ""
        if (caminho[i+1][0] > caminho[i][0]):
            aux = "E"
        elif(caminho[i+1][0] < caminho[i][0]):
            aux = "O"
        elif (caminho[i+1][1] > caminho[i][1]):
            aux = "S"
        elif(caminho[i+1][1] < caminho[i][1]):
            aux = "N"
        final += aux
    return final


caminho(mapa2)

# self.assertEqual(caminho(mapa1),"ESSSSSSEENNNEESSSSSEEESE")
# self.assertIn(caminho(mapa2),["EESS","SSEE"])
