# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
# seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = float(input("Digite a nota:\n"))

if nota > 10 or nota < 0:
    print("Valor inválido")
