"""
Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32
"""

import sys

a = input('Digite uma temperatura em Graus Celsius\n')

try:
    celsius = int(a)
except ValueError:
    try:
        celsius = float(a)
    except ValueError:
        print('Precisa ser um número')
        sys.exit(0)
        
fahreinheit = float(9 * celsius / 5 + 32)

print("O valor desta temperatura em Fahrenheit é de %.2f ºf" % fahreinheit)
