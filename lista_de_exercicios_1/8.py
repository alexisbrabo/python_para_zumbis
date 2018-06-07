"""
Faça agora o contrário, de Fahrenheit para Celsius.
Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32
"""

import sys

a = input('Digite uma temperatura em Graus Fahrenheit\n')

try:
    fahreinheit = int(a)
except ValueError:
    try:
        fahreinheit = float(a)
    except ValueError:
        print('Precisa ser um número')
        sys.exit(0)
        
celsius = float(5 / 9 * (fahreinheit - 32))

print("O valor desta temperatura em Celsius é de %.2f ºc" % celsius)
