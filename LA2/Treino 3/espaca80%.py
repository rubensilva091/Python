"""

Implemente uma função que, dada uma frase cujos espaços foram retirados, 
tenta recuperar a dita frase. Para além da frase (sem espaços nem pontuação), 
a função recebe uma lista de palavras válidas a considerar na reconstrução 
da dita frase. Deverá devolver a maior frase que pode construir inserindo
espaços na string de entrada e usando apenas as palavras que foram indicadas 
como válidas. Por maior entende-se a que recupera o maior prefixo da string
de entrada. Só serão usados testes em que a maior frase é única.

"""
palavras1 = ["e", "o", "so", "maior", "este", "curso", "urso", "es", "maio"]
palavras2 = ["o", "oga", "ga", "gato", "gatom", "mia",
             "eava", "ava", "e", "a", "va", "vaca", "mu", "muge"]


def espaca(frase, palavras):
    n = len(frase)
    cache = ["" for x in range(n+1)]

    for x in range(n):
        for y in range(x+1, n+1):
            pal = frase[x:y]
            if pal in palavras:
                ant = cache[x]
                if not cache[y]:
                    cache[y] = ant + " "*(ant != "") + pal
    return cache[n]


print(espaca("ogatomiaeavacamuge", palavras2))

# def test_espaca_1(self):
#    with test_timeout(self,2):
#        palavras = ["e","o","so","maior","este","curso","urso","es","maio"]
#        self.assertEqual(espaca("estecursoeomaior",palavras),"este curso e o maior")
#
# def test_espaca_2(self):
#    with test_timeout(self,2):
#        palavras = ["o","oga","ga","gato","gatom","mia","eava","ava","e","a","va","vaca","mu","muge"]
#        self.assertEqual(espaca("ogatomiaeavacamuge",palavras),"o gato mia e a vaca muge")
