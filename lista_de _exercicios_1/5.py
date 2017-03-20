# solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o
# preço a pagar.
import sys

a = input('Digite o Valor do Produto:\n')
try:
    a = float(a)
except ValueError:
    print('Precisa ser um número válido')
    sys.exit()

b = input('Digite a porcentagem do desconto:\n')
try:
    b = float(b)
except ValueError:
    print('Precisa ser um número válido')
    sys.exit()

c = a * (b / 100)
print('O valor do desconto é de %.2f Reais e o preço final ficará em %.2f Reais' % (c, a - c))