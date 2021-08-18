user = input("Digite seu Usuario: ")
senha = input("Digite sua Senha: ")

while user == senha:
    print("A senha e o usuario são iguais, por favor digite novamete")
    user = input("Digite seu Usuario: ")
    senha = input("Digite sua Senha: ")

print("A informações foram inseridas com sucesso!")