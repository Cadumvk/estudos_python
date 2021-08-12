numero_um = 2
numero_dois = 3

# faz a soma de dois numeros
soma = numero_um + numero_dois
# faz a subtração de dois numeros
sub = numero_um - numero_dois
# faz a multiplicação de dois numeros
multi = numero_um * numero_dois

print("A soma de {} e {} é igual a {}".format(numero_um,numero_dois,soma))
print(f"A subtração de {numero_um} e {numero_dois} é igual a {sub}")
print(f'A multiplicação de {numero_um} "e" {numero_dois} é igual a {multi}')

#essa é uma função que faz divisão
def divisao(num1,num2):
    div = num1 / num2
    return div

print(divisao(numero_um,numero_dois))
