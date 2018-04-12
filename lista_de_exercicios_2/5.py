# Faça um Programa que leia três números e mostre o maior e o menor deles.
a = int(input('Escreva o valor 1\n'))
b = int(input('Escreva o valor 2\n'))
c = int(input('Escreva o valor 3\n'))

list = [a, b, c]
list.sort()
print("O maior valor é " + str(list[len(list) - 1]) + ".\n" + "E o menor valor é " + str(list[0]) + ".")
