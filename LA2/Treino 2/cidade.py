'''
Podemos usar um (multi) grafo para representar um mapa de uma cidade: 
cada nó representa um cruzamento e cada aresta uma rua.

Pretende-se que implemente uma função que calcula o tamanho de uma cidade, 
sendo esse tamanho a distância entre os seus cruzamentos mais afastados.
NO FUNDO, Longest Path

A entrada consistirá numa lista de nomes de ruas (podendo assumir que os 
nomes de ruas são únicos). Os identificadores dos cruzamentos correspondem a 
letras do alfabeto, e cada rua começa (e acaba) no cruzamento 
identificado pelo primeiro (e último) caracter do respectivo nome.
'''

ruas1 = ["raio", "central", "liberdade", "chaos", "saovictor",
         "saovicente", "saodomingos", "souto", "capelistas", "anjo", "taxa"]

ruas2 = ["ab", "bc", "bd", "cd"]


# NAO SEI FAZER ESTA MERDA; NEM ENTENDI O ENUNCIADO CARALHOS
def tamanho(ruas):
    adj = {}

    # nao temos origem, logo meto um qualquer, safoda
    queue = [adj[0]]
    vis = {adj[0]}
    pai = {}
    while(queue):
        v = queue.pop(0)
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                pai[d] = v
                queue.append(d)
    return -1


# self.assertEqual(tamanho(ruas),25)
# self.assertEqual(tamanho(ruas),4)
