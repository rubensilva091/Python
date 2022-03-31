'''

Neste problema pertende-se calcular quais os vértices centrais
de um grafo pesado não orientado.

A excentricidade de um vértice é a distância desse vértice
ao vértice mais afastado. Os vértices centrais (ou centros) de
um grafo são os que tem excentricidade mínima.

Os vértices do grafo são identificados por letras do alfabeto.
O grafo será descrito através de uma sequência de arestas. Cada
aresta é descrita por uma string onde o primeiro e último caracteres
identificam os vértices adjacentes e os digitos no meio o peso da 
respectiva aresta.

A função deverá devolver a lista com todos os centros ordenados
alfabeticamente.

Se o grafo não for ligado deve devolver None.

'''


arestas1 = ["a5b", "b10c", "c4d", "a20d"]
arestas2 = ["a5b", "b10c", "c4d", "a20d", "e5f"]
arestas3 = ["ab"]

#Javardei isto  de uma maneira
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


def centros(arestas):
    adj = {}
    for r in arestas:
        if r[0] not in adj:
            adj[r[0]] = {}
        if r[-1] not in adj:
            adj[r[-1]] = {}

        # Colocar as arestas mais pequenas
        if r[0] not in adj[r[-1]]:
            adj[r[-1]][r[0]] = float("inf")

        if r[-1] not in adj[r[0]]:
            adj[r[0]][r[-1]] = float("inf")

        adj[r[0]][r[-1]] = min(int(r[1:len(r)-1]), adj[r[0]][r[-1]])
        adj[r[-1]][r[0]] = min(int(r[1:len(r)-1]), adj[r[-1]][r[0]])
    
    
    #Daqui pra baixo é um crime
    maior = float("inf")
    maior_var = ""
    aux_final = []
    is_connected = 0
    is_connected_aux = len(adj)

    for x in adj.keys():
        path = sorted(dijkstra(adj, x).items(), key=lambda i: (i[1], i[0]))
        is_connected = len(path)
        if is_connected != is_connected_aux:
            return None
        if maior > path[len(path)-1][1]:
            maior = path[len(path)-1][1]
            maior_var = path[0][0]
            aux_final = [path[0][0]]
        if(maior == path[len(path)-1][1]):
            if (path[0][0] not in aux_final):
                aux_final.append(path[0][0])

    return aux_final


print(centros(arestas3))

#self.assertEqual(centros(arestas), ['b'])
#self.assertEqual(centros(arestas), None)
