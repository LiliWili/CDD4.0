nomes = [""]*5
tam= len(nomes)
for i in range(tam):
    nomes[i]=input("Digite cinco nomes: ")
print(f"Nomes: {nomes}")
for x in range(tam-1,-1,-1):
    print(f"Ordem inversa dos nomes: {nomes[x]}")

nomes.reverse()
print(nomes)