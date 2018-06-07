# Escreva um programa para calcular a redução do tempo de vida de um fumante.
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
# Considere que um fumante perde 10 minutos de vida a cada cigarro,
"""
calcule quantos dias de vida um fumante perderá. Exiba o total de dias.
"""

quantidade = int(input("Quantidade de cigarros fumados por dia?\n"))
anos = int(input("Quantos anos sendo fumante?\n"))
dias = anos * 365
minutos = (quantidade * dias) * 10
total_dias = minutos / 1440
print('Você perderá %.4f dias' % total_dias)
