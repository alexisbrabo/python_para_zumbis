# determine se o ano é bissexto

ano = int(input("Digiite o ano\n"))

if ano % 4 == 0:
    if ano % 100 != 0:
        print("Ano Bissexto")
elif ano % 400 == 0:
    print("Ano Bissexto")
else:
    print("Ano não é Bissexto")
