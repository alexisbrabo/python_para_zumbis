# Escreva um programa que leia um valor em metros e o exiba convertido em milímetros

import sys

a = input('Escreva um valor em metros para ser convertido para milímetros\n')

try:
    metros = int(a)
except ValueError:
    try:
        metros = float(a)
    except ValueError:
        print('Precisa ser um número')
        sys.exit(0)

milimetros = float(metros * 1000)

print('%s metros equivalem a %.0f milímetros' % (a, milimetros))
