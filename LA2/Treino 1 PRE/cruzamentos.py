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

ruas1 = ["raio", "central", "liberdade", "chaos", "saovictor",
         "saovicente", "saodomingos", "souto", "capelistas", "anjo", "taxa"]
ruas2 = ["ab", "bc", "bd", "cd"]


def cruzamentos(ruas):
    dict_list = {}
    for rua in ruas:
        if ((not (rua[0] in dict_list.keys()))):
            dict_list.update({rua[0]: 0})
        dict_list[rua[0]] += 1
        if (not (rua[len(rua)-1] in dict_list.keys())):
            dict_list.update({rua[len(rua)-1]: 0})
        dict_list[rua[len(rua)-1]] += 1
        if (rua[0] == rua[len(rua)-1]):
            dict_list[rua[len(rua)-1]] -= 1
    dict_list = {k: v for (k, v) in sorted(dict_list.items(), key=lambda x: (-x[1], x[0]))}
    dict_list = {k: v for k, v in sorted(dict_list.items(), key=lambda item: item[1])}
    final = [(x,y) for (x,y) in dict_list.items()]
    return final


cruzamentos(ruas1)

# def test_cruzamentos_1(self):
#        with test_timeout(self,1):
#            self.assertEqual(cruzamentos(["raio","central","liberdade","chaos","saovictor","saovicente","saodomingos","souto","capelistas","anjo","taxa"]),[('t',1),('a',2),('e',2),('l',2),('r',2),('c',3),('o',3),('s',6)])
#
# def test_cruzamentos_2(self):
#        with test_timeout(self,1):
#            self.assertEqual(cruzamentos(["ab","bc","bd","cd"]),[('a',1),('c',2),('d',2),('b',3)])
