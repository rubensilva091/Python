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


def instrucoes(pai, d):
    instrucoes_path = ""
    while d in pai:
        if d[0] < pai[d][0]:
            instrucoes_path += "O"
        elif d[0] > pai[d][0]:
            instrucoes_path += "E"
        elif d[1] < pai[d][1]:
            instrucoes_path += "N"
        elif d[1] > pai[d][1]:
            instrucoes_path += "S"
        d = pai[d]
    return instrucoes_path[::-1]


def caminho(mapa):
    adj = {}
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    o = (0, 0)
    queue = [o]
    vis = {o}
    pai = {}
    while(queue):
        # Puxar da stack o proximo a ser percorrido e criar as suas edges
        v = queue.pop(0)
        if v not in adj:
            adj[v] = set()

        # Criar as edges
        for m in moves:
            nX = v[0]+m[0]
            nY = v[1]+m[1]
            if (nX >= 0 and nX < len(mapa[0]) and nY >= 0 and nY < len(mapa)):
                if mapa[nY][nX] != "#":
                    adj[v].add((nX, nY))

        # Visitar as edges
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                pai[d] = v
                queue.append(d)

    # Criar os comandos
    final = instrucoes(pai, (len(mapa[0])-1, len(mapa)-1))
    return final

# self.assertEqual(caminho(mapa1),"ESSSSSSEENNNEESSSSSEEESE")
# self.assertIn(caminho(mapa2),["EESS","SSEE"])
