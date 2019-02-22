"""
Faça um programa que calcule o aumento de um salário. Ele deve solicitar o
valor do salário e a
porcentagem do aumento. Exiba o valor do aumento e do novo salário.
"""

import sys

a = input('Digite o seu salário:\n')
try:
    a = float(a)
except ValueError:
    print('Precisa ser um número válido')
    sys.exit()

b = input('Digite a porcentagem do aumento:\n')
try:
    b = float(b)
except ValueError:
    print('Precisa ser um número válido')
    sys.exit()

c = a * (b / 100)
print('O valor do aumento é de %.2f Reais e o salário final ficará em %.2f Reais' % (c, a + c))
