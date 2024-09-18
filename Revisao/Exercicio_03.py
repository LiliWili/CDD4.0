# Receber dois valores e se eles forem iguais fazer a soma deles, se forem diferentes fazer
# a multiplicação dos numeros e no final dar a opção de repetir a operação ou não#
resp = 1
while resp != 2:
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))

    if a == b:
        c= a+b
        print(f"A soma dos dois numero é: {c}")
    else:
         c = a*b
         print(f"A multiplicação dos dois numeros é {c}")
    resp = input("Deseja repetir a operação? 1 para sim 2 para não")


