'''
O objectivo deste problema é determinar o tamanho do maior continente de um planeta.
Considera-se que pertencem ao mesmo continente todos os países com ligação entre si por terra. 
Irá receber uma descrição de um planeta, que consiste numa lista de fronteiras, onde cada fronteira
é uma lista de países que são vizinhos entre si. 
A função deverá devolver o tamanho do maior continente.
'''
vizinhos1 = [["Portugal", "Espanha"], ["Espanha", "França"], [
    "França", "Bélgica", "Alemanha", "Luxemburgo"], ["Canada", "Estados Unidos"]]
vizinhos2 = [["Portugal", "Espanha"], ["Espanha", "França"]]
vizinhos3 = [["Portugal"], ["Alemanha"]]
vizinhos4 = []


def bfs_continente(adj):
    final_pai = []
    for o in adj.keys():
        queue = [o]
        vis = {o}
        pai = {}
        while(queue):
            v = queue.pop(0)
            for d in adj[v]:
                if d not in vis:
                    vis.add(d)
                    pai[d] = v
                    queue.append(d)
        final_pai.append(pai)
    return final_pai


def maior(vizinhos):
    adj = {}
    for fronteira in vizinhos:
        # sem esta linha de codigo toda FODIDA e completamente errada logicamente, o programa da 60%
        # Isto é, por causa da minha iteraçao, se existir fronteiras com 1 ou menos, FUDEU, nao vai iterar,
        # Logo, meti qualquer merda dentro da adj[fronteira[0]] e ficou a funcionar, Whatever
        if len(fronteira) == 1:
            print(fronteira)
            adj[fronteira[0]] = fronteira

        # De resto, está cleanzaçooo (jk, isto está javardo pra caralho)
        for i in range(len(fronteira)-1):
            if fronteira[i] not in adj:
                adj[fronteira[i]] = set()
            if fronteira[i+1] not in adj:
                adj[fronteira[i+1]] = set()
            adj[fronteira[i]].add(fronteira[i+1])
            adj[fronteira[i+1]].add(fronteira[i])

    path = bfs_continente(adj)
    # ordernar todos PELA quantidade de edges, assim obtemos Na primeira posiçao um continente qualquer, mas que contem o maior nr de edges
    path = sorted(path, key=lambda i: -len(i))

    # Pode ser vazio, logo, nao path[0] nao existe e FODEU
    final_path = 0
    if path:
        final_path = len(path[0])+1
    return final_path


print(maior(vizinhos4))
#self.assertEqual(maior(vizinhos), 6)
#self.assertEqual(maior(vizinhos), 3)
