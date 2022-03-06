'''
Podemos usar um (multi) grafo para representar um mapa de uma cidade: 
cada nó representa um cruzamento e cada aresta uma rua.

Pretende-se que implemente uma função que lista os cruzamentos de uma cidade 
por ordem crescente de criticidade: um cruzamento é tão mais crítico quanto 
maior o número de ruas que interliga.

A entrada consistirá numa lista de nomes de ruas (podendo assumir que os nomes de ruas são únicos). 
Os identificadores dos cruzamentos correspondem a letras do alfabeto, e cada rua começa (e acaba) no cruzamento 
identificado pelo primeiro (e último) caracter do respectivo nome.

A função deverá retornar uma lista com os nomes dos cruzamentos por ordem crescente de criticidade, 
listando para cada cruzamento um tuplo com o respectivo identificador e o número de ruas que interliga.
Apenas deverão ser listados os cruzamentos que interliguem alguma rua, e os cruzamentos com o mesmo 
nível de criticidade deverão ser listados por ordem alfabética.
'''

ruas1 = ["ab","bc","bd","cd"]
ruas2 = ["raio","central","liberdade","chaos","saovictor","saovicente","saodomingos","souto","capelistas","anjo","taxa"]

def cruzamentos(ruas):
    grafos = []
    ruas_usadas=[]
    for r in ruas:
        aux = [r[0],r[len(r)-1]]
        for a in aux:
            if(a not in ruas_usadas):
                grafos.append((a,1))
                ruas_usadas.append(a)
            else:
                pos=0
                for (k,v) in grafos:
                    if (k==a):
                        grafos[pos] = (k,v+1)
                    pos+=1
        if (aux[0]==aux[1]):
            grafos[pos-1] = (k,v)
    new_grafos= sorted(grafos)
    return sorted(new_grafos, key=lambda i: i[1])

print(cruzamentos(ruas2))


#def test_cruzamentos_1(self):
#        with test_timeout(self,1):
#            self.assertEqual(cruzamentos(["raio","central","liberdade","chaos","saovictor","saovicente","saodomingos","souto","capelistas","anjo","taxa"]),[('t',1),('a',2),('e',2),('l',2),('r',2),('c',3),('o',3),('s',6)])
#
#def test_cruzamentos_2(self):
#        with test_timeout(self,1):
#            self.assertEqual(cruzamentos(["ab","bc","bd","cd"]),[('a',1),('c',2),('d',2),('b',3)])
            