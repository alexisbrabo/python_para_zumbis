#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
#usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
#sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

km = float(input('Kilometros rodados:\n'))
dias = float(input('Dias de aluguel\n'))

precoapagar = float(60 * dias + km * 0.15);

print('Preço a pagar: R$ %.2f' % precoapagar)
