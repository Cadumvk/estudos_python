valores = input().split(" ")
A = float(valores[0])
B = float(valores[1])
C = float(valores[2])
delta = float((B ** 2) - (4 * A * C))

if (A == 0 or delta < 0):
    print("Impossivel calcular")
else:
    R1 = ((B * -1) + (delta ** 0.5)) / (2 * A)
    R2 = ((B * -1) - (delta ** 0.5)) / (2 * A)
    print("R1 = {:.5f}\nR2 = {:.5f}".format(R1,R2))
    # print("R2 = {:.5f}".format(R2))