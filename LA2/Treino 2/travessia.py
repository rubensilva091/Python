'''
Implemente uma função que calcula o menor custo de atravessar uma região de
Norte para Sul. O mapa da região é rectangular, dado por uma lista de strings,
onde cada digito representa a altura de cada ponto. Só é possível efectuar 
movimentos na horizontal ou na vertical, e só é possível passar de um ponto
para outro se a diferença de alturas for inferior ou igual a 2, sendo o custo 
desse movimento 1 mais a diferença de alturas. O ponto de partida (na linha
mais a Norte) e o ponto de chegada (na linha mais a Sul) não estão fixados à
partida, devendo a função devolver a coordenada horizontal do melhor
ponto para iniciar a travessia e o respectivo custo. No caso de haver dois pontos
com igual custo, deve devolver a coordenada mais a Oeste.
'''

mapa1 = ["4563",
         "9254",
         "7234",
         "3231",
         "3881"]

mapa2 = ["90999",
         "00000",
         "92909",
         "94909"]

mapa3 = ["000",
         "888",
         "111"]


def travessia(mapa):
    final=[]
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    #Fazer a travessia em cada ponto da primeira linha
    for i in range(len(mapa[0])):
        adj = {}
        pai = {}
        dist = {}
        o = (i, 0)
        dist[o] = 0
        orla = {o}
        while orla:
            v = min(orla, key=lambda x: dist[x])
            orla.remove(v)
            if v not in adj:
                adj[v] = {}

            # Criar as edges
            for m in moves:
                new_X = v[0]+m[0]
                new_Y = v[1]+m[1]
                new_coord = (new_X, new_Y)
                if (new_X >= 0 and new_X < len(mapa[0]) and new_Y >= 0 and new_Y < len(mapa)):
                    altura = abs(int(mapa[v[1]][v[0]])-int(mapa[new_Y][new_X]))
                    if new_X<i and new_Y==0:
                        altura=99
                    if(altura <= 2):
                        adj[v][new_coord] = altura+1
                            

            # Percorrer as edges
            for d in adj[v]:
                if d not in dist:
                    orla.add(d)
                    dist[d] = float("inf")
                if dist[v] + adj[v][d] < dist[d]:
                    pai[d] = v
                    dist[d] = dist[v] + adj[v][d]

        #Obter a coordenada mais a oeste
        aux=[]
        for ((v1,v2),v3) in dist.items():
            if v2==len(mapa)-1:
                aux.append((i,v1,v2, v3))
        if len(aux)>0:
            final.append(sorted(aux, key=lambda i:(i[3],i[1])).pop(0))

    #Criar a variavel final
    final=sorted(final, key=lambda i:(i[3],i[1])).pop(0)
    return (final[0],final[3])

# self.assertEqual(travessia(mapa1),(2,10))
# self.assertEqual(travessia(mapa2),(1,5))
