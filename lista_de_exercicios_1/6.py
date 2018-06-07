# Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média
# esperada para a viagem.
import sys

a = input('Qual a distância a ser percorrida?\n')
try:
    a = float(a)
except ValueError:
    print('Precisa ser um número')
    sys.exit(0)

b = input('Qual a velocidade média esperada?\n')
try:
    b = float(b)
except ValueError:
    print('Precisa ser um número')
    sys.exit(0)

c = a / b;

print('O tempo médio desta viagem será de %.2f horas' % c)