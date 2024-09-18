#fazer a divisao de dois numeros e se o segundo numero for igual a 0, peça que ele digite um numero valido#

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
n= 0
while num2 == 0:
    print("Digite um valor diferente de zero")
    num2 = int(input("Digite o segundo numero: "))
divisao = num1 / num2
print(f"O resultado da divisão é: {divisao}")
