valor = int(input(""))
notas = [100,50,20,10,5,2,1]

print(valor)

for nota in notas:
    quantidade_nota = int(valor / nota)
    print("{} nota(s) de R$ {},00".format(quantidade_nota,nota))
    valor -= quantidade_nota * nota

