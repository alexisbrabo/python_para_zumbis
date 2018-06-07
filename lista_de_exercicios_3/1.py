"""
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido
e continue pedindo até que o usuário informe um valor válido
"""

nota = int(input("Digite a nota:\n"))

while nota > 10 or nota < 0:
    print("Nota Inválida:\n")
    nota = int(input("Digite a nota:\n"))
