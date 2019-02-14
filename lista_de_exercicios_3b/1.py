"""
 Dizemos que um número natural é triangular se ele é produto de três números
naturais consecutivos. Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um
inteiro não-negativo n,
verificar se n é triangular.
"""

numero = int(input("Digite um número inteiro não negativo\n"))

i = 0

while i * (i+1) * (i+2) < numero:
    i += 1

if i * (i+1) * (i+2) == numero:
    print("É triangular!")
else:
    print("Não é triangular!")
