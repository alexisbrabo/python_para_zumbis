"""
Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. 
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos
intercalados dos dois outros vetores. Imprima os três vetores.
"""
import random

lista = []
lista2 = []
i = 0

while i < 10:
    lista.append(random.randint(1, 100))
    lista2.append(random.randint(1, 100))
    i = i + 1

lista3 = lista + lista2

print(lista)
print(lista2)
print(lista3)