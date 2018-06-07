# Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado
# a um milhão.
a = 2 ** 1000000
b = str(a)
print("O número de digitos do resultado é %s " % len(b))
