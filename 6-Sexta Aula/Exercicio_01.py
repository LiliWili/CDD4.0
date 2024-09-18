#Ler duas notas e imprimir a media do aluno mas enquanto a nota for maior que 10 e menor que 0, pedir
# pra digitar novamente#

nota1 = float(input("Digite a primeira nota: "))
while nota1 <0 or nota1 >10:
    nota1 = float(input("Digite a primeira nota novamente: "))

nota2 = float(input("Digite a segunda nota: "))
while nota2 <0 or nota2 >10:
    nota2 = float(input("Digite a segunda nota novamente: "))

media= (nota1+nota2)/2
print(f"A media do aluno é: {media}")

#Digitar o numero 5 e sair cada numero subsequente a ele na quantidade de vezes que ele é#

n = int(input("Digite um numero: "))
for x in range(1, n+1):
    for n in range(1, x +1):
        print(x, end= " ")
