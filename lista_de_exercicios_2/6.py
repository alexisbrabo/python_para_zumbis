# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#  Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
#  faça um programa que nos dê o salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato e o salário líquido.
#  Observe que Salário Bruto - Descontos = Salário Líquido.
#  Calcule os descontos e o salário líquido, conforme a tabela abaixo:
#  a. + Salário Bruto : R$ b. - IR (11%) : R$ c. - INSS (8%) : R$ d. - Sindicato ( 5%) : R$ e. = Salário Liquido : R$

valor = float(input("Quanto você ganha por hora?\n"))
numHoras = float(input("Número de Horas trabalhadas\n"))
bruto = valor * numHoras
descontoImpostoRenda = (11 / 100) * bruto
descontoInss = (8 / 100) * bruto
descontoSindicato = (5 / 100) * bruto
salarioLiquido = bruto - descontoImpostoRenda - descontoInss - descontoSindicato

print("Seu salário bruto é de %.2f Reais" % bruto)
print("Seu desconto de Imposto de Renda foi de %.2f Reais" % descontoImpostoRenda)
print("Seu desconto de INSS foi de %.2f Reais" % descontoInss)
print("Seu desconto de Sindicato foi de %.2f Reais" % descontoSindicato)
print("Seu salário líquido é de %.2f Reais" % salarioLiquido)
