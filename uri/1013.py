valores = input().split(" ")
A = int(valores[0])
B = int(valores[1])
C = int(valores[2]) 

MaiorAB = (A + B + abs(A - B)) / 2
resultado = (MaiorAB + C + abs(MaiorAB - C)) / 2

print("{} eh o maior".format(int(resultado)))