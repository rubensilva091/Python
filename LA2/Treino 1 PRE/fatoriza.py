'''
Defina uma função que recebe um número positivo
e produz a soma dos seus factores primos distintos.
'''
import time


n1 = 6
n2 = 28


def factoriza(n):
    final = []
    while(n > 1):
        counter = 2
        while(n % counter != 0):
            counter += 1
            if (n % counter == 0):
                break
        n = n/counter
        if(not counter in final):
            final.append(counter)
    resultado = sum(final)
    return resultado


factoriza(28)

# def test_factoriza_1(self):
#    with test_timeout(self,1):
#        self.assertEqual(factoriza(6),5)
#
# def test_factoriza_2(self):
#    with test_timeout(self,1):
#        self.assertEqual(factoriza(28),9)
