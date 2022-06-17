'''

Implemente a função filtra por forma a filtrar as strings que concordam com um padrão.
Uma string concorda com um padrão se for possível obtê-la a partir
do padrão substituindo cada caracter '?' por uma letra e cada caracter '*' por um
número arbitrário de letras. Por exemplo, 'aabxaxb' concorda com o padrão 'a*?b',
enquanto que 'ab' já não.

'''



padrao1 = "a?*"
strings1 = ["abc", "aabbc", "a", "baaa"]


def filtra(padrao, strings):
    if (len(padrao)==0):
        return [""]


    for i in range(len(padrao)):
        for str in strings:
            if len(str) <= i and padrao[i] != "*":
                strings.remove(str)
            elif padrao[i] == "?":
                continue
            elif padrao[i] == "*" :
                continue
            elif padrao[i] != str[i]:
                strings.remove(str)

    return strings


print(filtra(padrao1, strings1))

# def test_filtra_0(self):
#    with test_timeout(self,1):
#        padrao = "a?*"
#        strings = ["abc","aabbc","a","baaa"]
#        self.assertEqual(filtra(padrao,strings), ['abc','aabbc'])
#
# def test_filtra_1(self):
#    with test_timeout(self,1):
#        padrao = "??a*"
#        strings = ["abc","aaabc","aba","baaa"]
#        self.assertEqual(filtra(padrao,strings), ['aaabc','aba','baaa'])
