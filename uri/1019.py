segundos = int(input(""))
quantidade_segundos = [3600,60,1]
hms = []

for segundo in quantidade_segundos:
    qtd_segundos = int(segundos / segundo)
    hms.append(str(qtd_segundos))
    segundos -= qtd_segundos * segundo

print(":".join(hms))
