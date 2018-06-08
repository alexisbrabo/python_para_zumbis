"""
Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa 
anual de crescimento de 3% e que a população de B seja 200.000 habitantes com uma taxa de 
crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos 
necessários para que a população do país A ultrapasse ou iguale a população do país B, 
mantidas as taxas de crescimento
"""

populacao_a = 80000
tx_crescimento_a = 3.0
populacao_b = 200000
tx_crescimento_b = 1.5

i = 0

while populacao_a < populacao_b:
    populacao_a = populacao_a + ((tx_crescimento_a/100) * populacao_a)
    populacao_b = populacao_b + ((tx_crescimento_b/100) * populacao_b)
    i = i + 1

print("Levou %d anos para a população A ultrapassar a população B" % i)