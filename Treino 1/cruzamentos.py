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
    cruzamento = {}

    for n in ruas:
        cruzamento1=n[0]
        cruzamento2=n[len(n)-1]

        #inicilizar os cruzamentos
        if(cruzamento1 not in cruzamento):
            cruzamento[cruzamento1]=1
        if (cruzamento2 not in cruzamento):
            cruzamento[cruzamento2]=1

        #incrementar os cruzamentos
        for key,value in cruzamento.items():
            if (key==cruzamento1):
                cruzamento[key] = value+1
            if (key==cruzamento2):
                cruzamento[key] = value+1

    #criar a lista final, NAO SEI O PQ, mas todos os values estavam com 1 a mais
    lista_final = [(key,value-1) for key,value in sorted(cruzamento.items(), key=lambda i:(i[1],i[0]))]
    return lista_final


#self.assertEqual(cruzamentos(["raio","central","liberdade","chaos","saovictor","saovicente","saodomingos","souto","capelistas","anjo","taxa"]),[('t',1),('a',2),('e',2),('l',2),('r',2),('c',3),('o',3),('s',6)])
#elf.assertEqual(cruzamentos(["ab","bc","bd","cd"]),[('a',1),('c',2),('d',2),('b',3)])
            