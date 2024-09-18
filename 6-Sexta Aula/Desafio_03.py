#digitar o numero 9 e sair um triangulo#

n = int(input("Digite um numero: "))
for x in range(0, n+1):
    for y in range(0, x +1):
        print(y, end = "")
    print()
