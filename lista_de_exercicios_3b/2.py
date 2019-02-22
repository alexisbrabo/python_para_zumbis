"""
Indique como um troco deve ser dado utilizando-se um número mínimo de notas.
Seu algoritmo deve ler o valor da conta a ser paga e o valor do pagamento
efetuado desprezando os centavos. Suponha que as notas para troco sejam as de
50, 20, 10, 5, 2 e 1 reais, e que
nenhuma delas esteja em falta no caixa.
"""

valor_conta = int(input("Valor da conta:\n"))

valor_pagamento = int(input("Valor do pagamento\n"))

if (valor_pagamento < valor_conta):
    print("O valor do pagamento não pode ser menor do que o valor da conta!")
elif (valor_pagamento == valor_conta):
    print("Não precisa de troco!")
else:
    valor_troco = valor_pagamento - valor_conta
    texto = ""
    soma = 0
    while soma != valor_conta:dddd
        
