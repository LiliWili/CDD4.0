num = [0]*10
tam= len(num)
cont=0
for i in range(tam):
    num[i]=int(input("Digite dez numeros: "))
qlq=int(input("Digite um numero aleatorio: "))
for x in range(tam):
    if num[x] == qlq:
        cont+= 1
print(f"o numero {qlq} se repete {cont} vezes")
