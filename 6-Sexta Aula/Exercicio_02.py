#Refazer o exercicio anterior com a pergunta "deseja realizar novo calculo?"#
calculo = 1
while calculo != 2:

    nota1 = float(input("Digite a primeira nota: "))
    while nota1 < 0 or nota1 > 10:
        nota1 = float(input("Digite a primeira nota novamente: "))

    nota2 = float(input("Digite a segunda nota: "))
    while nota2 < 0 or nota2 > 10:
        nota2 = float(input("Digite a segunda nota novamente: "))

    media = (nota1 + nota2) / 2
    print(f"A media do aluno é: {media}")
    calculo = int(input("Deseja fazer um novo calculo? 1 para sim 2 para nao: "))