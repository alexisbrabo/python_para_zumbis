"""
Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, 
sem usar as funções max e min
"""

import random

lista = []
i = 0

while i < 20:
    lista.append(random.randint(1, 1000))
    i = i + 1

print(lista)

lista.sort()

print("O maior valor é %d" % lista[0])
print("O menor valor é %d" % lista[len(lista)-1])