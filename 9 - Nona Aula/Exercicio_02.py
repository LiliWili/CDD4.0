numeros = [0]*10
tam= len(numeros)
cont=0


for i in range(tam):
    numeros[i]=int(input("Digite dez valores: "))
numMaior=numeros[0]
numMenor =numeros[0]
soma=0
for x in range(tam):
    if numeros[x]%2==0:
        print(f"Os numeros pares são {numeros[x]}")

for w in range(tam):
    if numMaior < numeros[w]:
        numMaior = numeros[w]
print(f"O maior numero é: {numMaior}")

for m in range(tam):
    if numeros[m] < numMenor:
        numMenor = numeros[m]
print(f"O menor numero é: {numMenor}")

for o in range(tam):
    soma += numeros[o]
media = soma / tam
for y in range(tam):
    if numeros[y] > media:
        cont=cont+1
print(f"A media dos valores é {media} e os valores acima da media são {cont}")