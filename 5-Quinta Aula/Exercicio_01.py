contagem = 0
for n in range (10):
    num = float(input("Digite um valor: "))
    if num < 0:
        contagem = contagem + 1
print (f"Os numeros negativos são: {contagem}")
