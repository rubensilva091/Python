'''
Defina uma função que recebe um número positivo
e produz a soma dos seus factores primos distintos.
'''


def factoriza(n):
    # Fatorizar o elemento
    divisor = 1
    elementos_unicos = []
    while(n != 1):
        divisor += 1
        if(n % divisor == 0):
            n = n/divisor
            # Encontrar os elementos unicos
            if (divisor not in elementos_unicos):
                elementos_unicos.append(divisor)
            divisor = 1
    return sum(elementos_unicos)

# self.assertEqual(factoriza(6),5)
# self.assertEqual(factoriza(28),9)
