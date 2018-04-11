# Faça um Programa que leia três números e mostre o maior deles.
a = int(input('Escreva o lado 1 do triângulo\n'))
b = int(input('Escreva o lado 2 do triângulo\n'))
c = int(input('Escreva o lado 3 do triângulo\n'))

list = [a, b, c]
list.sort()
print("O maior valor é " + str(list[len(list) - 1]))
