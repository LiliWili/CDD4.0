#Receber 3 numeros e dizer se a soma dos dois primeiros numeros é maior que o terceiro numero recebido#
a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
c = int(input("Digite o terceiro numero: "))

soma = a+b

if soma > c:
    print(f"a soma a+b={soma} é maior que o numero da letra c={c}")
elif soma == c:
    print(f"A soma a+b={soma} é igual o numero da letra c={c}")
else:
    print(f"a soma de a+b={soma} é menor que o numero da letra c={c}")