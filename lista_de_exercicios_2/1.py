# Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
#  Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno

a = int(input('Escreva o lado 1 do triângulo\n'))
b = int(input('Escreva o lado 2 do triângulo\n'))
c = int(input('Escreva o lado 3 do triângulo\n'))

if abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b:
    print("É triângulo")
    if a == b == c:
        print("É equilátero")
    elif a == b or b == c or a == c:
        print("É isósceles")
    else:
        print("É escaleno")
else:
  print("Não é triângulo")
