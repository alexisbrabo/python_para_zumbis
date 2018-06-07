# Faça um programa que peça dois números inteiros e imprima a soma desses dois números
import sys

a = input('Digite o primeiro número inteiro\n')

try:
    valor1 = int(a)
except ValueError:
    print('O número deve ser inteiro')
    sys.exit()

b = input('Digite o segundo número inteiro\n')
try:
    valor2 = int(b)
except ValueError:
    print('O número deve ser inteiro')
    sys.exit()

print(valor1 + valor2)
