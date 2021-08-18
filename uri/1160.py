T = int(input(""))

for test in range(0,T):
    dados = input().split(" ")
    PA = int(dados[0])
    PB = int(dados[1])
    G1 = float(dados[2])/100
    G2 = float(dados[3])/100
    ano = 0
    while True:
        PA += int(PA * G1)
        PB += int(PB * G2)
        ano += 1
        if PA > PB or ano > 100:
            break

    if ano <= 100:
        print("{} anos.".format(ano))
    else:
        print("Mais de 1 seculo.")


