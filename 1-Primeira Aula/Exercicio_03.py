nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
meses = idade*12
salario = float(input("Digite seu salario: "))
aumento= (salario*1.1)
#1.1 é acrescimo de 10% do salario, se for 20 é 1.2 e assim segue
print(f"Seu nome é: {nome}, você tem {idade} anos e {meses} meses, você recebe US${aumento}")