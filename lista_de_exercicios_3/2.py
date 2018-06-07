"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao
nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
"""

nome = input("Digite o nome de usuário\n")
senha = input("Digite a senha\n")

while nome == senha:
    print("O nome e a senha não podem ser iguais!")
    nome = input("Digite o nome de usuário\n")
    senha = input("Digite a senha\n")

print("Ok")
