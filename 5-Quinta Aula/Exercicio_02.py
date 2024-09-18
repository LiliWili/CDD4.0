#Ler 10 numeros e mostrar quantos estao dentro do intervalo entre 10 e 20 e fora do intervalo#
contagem = 0
cont = 0
for n in range (20):
    num = float(input("Digite um valor: "))
    if num > 10 and num < 20:
        contagem = contagem + 1
    else:
        cont = cont + 1

print(f"Os numeros dentro do intervalo são: {contagem}")
print(f"Os numeros fora do intervalo são: {cont}")

#Jeito sem else e com apenas uma variavel#
contagem = 0
for n in range (10):
    num = int(input("Digite um valor: "))
    if num > 10 and num < 20:
        contagem = contagem + 1

print(f"Os numeros dentro do intervalo são: {contagem} e os numeros dentro do intervalo são: {10-contagem}")