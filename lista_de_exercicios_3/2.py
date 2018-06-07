# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao
# nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.


def verificarlogin():
    nome = input("Digite o nome de usuário\n")
    senha = input("Digite a senha\n")
    if nome == senha:
        return True
    else:
        return False


while verificarlogin():
    print("O nome e a senha não podem ser iguais!")

print("Ok")
