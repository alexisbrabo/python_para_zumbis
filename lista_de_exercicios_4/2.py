"""
Sorteie 20 inteiros entre 1 e 100 numa lista.
Armazene os números pares na lista PAR e os números ímpares na lista IMPAR. 
Imprima as três listas
"""
import random

lista = []
lista_par = []
lista_impar = []

i = 0

while i < 20:
    lista.append(random.randint(1, 1000))
    if (lista[len(lista)-1] % 2 == 0):
        lista_par.append(lista[len(lista)-1])
    else:
        lista_impar.append(lista[len(lista)-1])
    i = i + 1

print(lista)
print(lista_par)
print(lista_impar)
