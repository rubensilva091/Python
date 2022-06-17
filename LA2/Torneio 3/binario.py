'''

Implemente uma função que calcula quantas sequências de n bits existem onde
não aparecem dois 1s seguidos.

Sugere-se que começe por definir uma função recursiva que calcula quantas 
sequências de n bits começadas por um dado bit existem onde não aparecem 
dois 1s seguidos.

'''

def binario(n):

    #Se for 0
    if n==0:
        return 0

    #Criaçao da cache
    cache1=[0 for i in range(n)]
    cache2=[0 for i in range(n)]
    cache1[0] = 1
    cache2[0] = 1



    for i in range(n):
        if i ==0:
            continue
        else:
            cache1[i] = cache1[i-1] + cache2[i-1]
            cache2[i] = cache1[i-1]

    return cache1[n-1] + cache2[n-1]
 
# Driver program to test
# above functions
 
print(binario(5))




#    def test_binario_0(self):
#        with test_timeout(self,1):
#            self.assertEqual(binario(5),13)
#
#    def test_binario_1(self):
#        with test_timeout(self,1):
#            self.assertEqual(binario(10),144)    