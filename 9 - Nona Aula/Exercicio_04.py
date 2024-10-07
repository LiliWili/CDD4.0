def somar3(*numeros):
    soma = 0
    tam=len(numeros)
    for i in range(tam):
        soma = soma +numeros[i]
    print(soma)

def letras(texto):
    tam=len(texto)
    cont=0
    for i in texto:
        if i not in " ":
           cont+=1
    print(f"O texto tem {cont} letras")
    for x in range(tam-1,-1,-1):
        print(texto[x], end="")
    print("\nou")
    print(texto[::-1])