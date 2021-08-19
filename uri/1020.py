idade_dias = int(input(""))
dias = [365,30,1]
resultado = []

for dia in dias:
    qtd_dias = int(idade_dias / dia)
    resultado.append(qtd_dias)
    idade_dias -= qtd_dias * dia

print("{} ano(s)".format(resultado[0]))
print("{} mes(es)".format(resultado[1]))
print("{} dia(s)".format(resultado[2]))