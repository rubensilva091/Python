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

def bfs(adj, o):
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
    return pai

def maior(vizinhos):
    adj = {}
    #Gerar o grafo de fronteiras
    for continente in vizinhos:
        for pais in continente:
            for i in range(len(continente)):
                if pais not in adj:
                    adj[pais] = set()
                if pais != continente[i]:
                    adj[pais].add(continente[i])

    #Obter o maior continente
    maior=0
    for p in adj:
        n= len(bfs(adj,p)) +1
        if(n>maior):
            maior=n

    return maior

#self.assertEqual(maior(vizinhos), 6)
#self.assertEqual(maior(vizinhos), 3)
