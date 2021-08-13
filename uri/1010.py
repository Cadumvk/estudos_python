peca1 = input().split(" ")

codep1 = int(peca1[0])
nump1 = int(peca1[1])
valorp1 = float(peca1[2])

peca2 = input().split(" ")

codep2 = int(peca2[0])
nump2 = int(peca2[1])
valorp2 = float(peca2[2])

pegar = (nump1 * valorp1) + (nump2 * valorp2)

print("VALOR A PAGAR: R$ {:.2f}".format(pegar))