'''

O objectivo deste problema é determinar quantos movimentos são necessários para 
movimentar um cavalo num tabuleiro de xadrez entre duas posições.
A função recebe dois pares de coordenadas, que identificam a origem e destino pretendido,
devendo devolver o número mínimo de saltos necessários para atingir o destino a partir da origem.
Assuma que o tabuleiro tem tamanho ilimitado.

'''
salto1Origem = (0, 0)
salto1Destino = (1, 1)
salto2Origem = (0, 0)
salto2Destino = (7, 7)


def saltos(o, d):
    adj = {}
    queue = [o]
    visited = {o}
    path = {}
    path[o] = o
    # os movimentos que o cavalo pode fazer num tabuleiro de chess
    moves = [(2, 1), (2, -1), (-2, -1), (-2, 1),
             (1, 2), (-1, 2), (1, -2), (-1, -2)]

    # se o destino e a origem coinciderem nem vale apena fazer calculos
    if d == o:
        return 0

    # bfs
    while(queue):
        node = queue.pop(0)

        # criaçao das edges
        if (node not in adj):
            adj[node] = set()
        for mov in moves:
            adj[node].add((node[0]+mov[0], node[1]+mov[1]))

        # percorrer as edges
        for new_node in adj[node]:
            if new_node not in visited:
                visited.add(new_node)
                path[new_node] = node
                queue.append(new_node)

            # se já existir, baza
            if new_node == d:
                queue = []
                break

    # shortest path
    caminho = [d]
    while d in path:
        d = path[d]
        caminho.insert(0, d)
        if d == o:
            break
    return len(caminho) - 1


print(saltos(salto2Origem, salto2Destino))
# self.assertEqual(saltos1((0,0),(1,1)),2)
# self.assertEqual(saltos2((0,0),(7,7)),6)
