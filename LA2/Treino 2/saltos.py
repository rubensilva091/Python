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
salto3Origem = (0, 0)
salto3Destino = (0, 0)

def shortest_path(pai, o, d):
    caminho = [d]
    while d in pai:
        d = pai[d]
        caminho.insert(0, d)
    return caminho

def saltos(o, dest):
    adj = {}
    # os movimentos que o cavalo pode fazer num tabuleiro de chess
    moves = [(2, 1), (2, -1), (-2, -1), (-2, 1),
             (1, 2), (-1, 2), (1, -2), (-1, -2)]
    queue = [o]
    vis = {o}
    pai = {}
    while(queue):
        v = queue.pop(0)
        if v not in adj:
            adj[v] = set()

        #Tods os movimentos do cavalo no xadrez
        for m in moves:
            adj[v].add((v[0]+m[0], v[1]+m[1]))

        #Percorrer as edges
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                pai[d] = v
                queue.append(d)

            #Parar o ciclo
            if d==dest:
                queue=[]
                break
    #Caminho mais curto
    path=shortest_path(pai, o, dest)
    return len(path)-1

# self.assertEqual(saltos1((0,0),(1,1)),2)
# self.assertEqual(saltos2((0,0),(7,7)),6)
