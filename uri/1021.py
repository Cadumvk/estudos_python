dinheiro = float(input(""))
notas = [100.00,50.00,20.00,10.00,5.00,2.00]
moedas = [1.00,0.50,0.25,0.10,0.05,0.01]
print("NOTAS:")
for nota in notas:
    quantidade_nota = int(dinheiro / nota)
    print("{} nota(s) de R$ {:.2f}".format(quantidade_nota,nota))
    dinheiro -= quantidade_nota * nota 
print("MOEDAS:")
for moeda in moedas:
    quantidade_moeda = int(round(dinheiro,2) / moeda)
    print("{} moeda(s) de R$ {:.2f}".format(quantidade_moeda,moeda))
    dinheiro -= quantidade_moeda * moeda
