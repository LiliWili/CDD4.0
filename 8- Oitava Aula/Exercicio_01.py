nomes = [" "]*5
senhas = [0]*5
tam= len(nomes)
for i in range(tam):
    nomes[i]=input("Digite seu nome: ")
    senhas[i]=int(input("Digite sua senha: "))
for x in range(tam):
    print(f"Posição: {x} Titular: {nomes[x]} Senha: {senhas[x]}")

