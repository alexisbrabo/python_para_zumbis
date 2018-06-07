"""
Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário.
Calcule o total em segundos.
"""

import sys

a = input('Digite o número de dias\n')

try:
    a = int(a)
except ValueError:
    try:
        a = float(a)
    except ValueError:
        print('Precisa ser um número')
        sys.exit(0)

b = input('Digite o número de horas\n')

try:
    b = int(b)
except ValueError:
    try:
        b = float(b)
    except ValueError:
        print('Precisa ser um número')
        sys.exit(0)

c = input('Digite o número de minutos\n')

try:
    c = int(c)
except ValueError:
    try:
        c = float(c)
    except ValueError:
        print('Precisa ser um número')
        sys.exit(0)

d = input('Digite o número de segundos\n')

try:
    d = int(d)
except ValueError:
    try:
        d = float(d)
    except ValueError:
        print('Precisa ser um número')
        sys.exit(0)

diasParaSegundos = a * ((24 * 60) * 60)
horasParaSegundos = (b * 60) * 60
minutosParaSegundos = c * 60

print('O total de tudo isso em segundos é:', diasParaSegundos + horasParaSegundos + minutosParaSegundos + d)
