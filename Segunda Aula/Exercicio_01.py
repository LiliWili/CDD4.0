#Receber dois numeros e printar em ordem crescente ou se são numeros iguais
a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
if a > b:
    print(b, a)
else:
    if b > a:
        print(a, b)
    else:
        print(f"Numeros iguais")
