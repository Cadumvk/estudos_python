num = int(input("Digite um numero inteiro!"))

resultado = num % 2

if resultado == 1:
    print("O numero {} é impar!".format(num))
else:
    print("O numero {} é par!".format(num))