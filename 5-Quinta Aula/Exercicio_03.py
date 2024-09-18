#Receber 10 notas e mostrar a media aritmetica dos 10 valores

n= 0
soma = 0
while n < 10:
    valores = int(input("Digite um valor: "))
    n = n+1
    soma = soma + valores
media = soma/10
print(f"A média aritmética dos valores é: {media}")