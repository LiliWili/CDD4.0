#Ler as notas de 5 alunos e guardar num vetor, calcular a media e contar quantos alunos tiverem nota
# acima da media#

nomes = ["Jordy","Wiliane","Mariana","Lucas","Eduarda"]
notas = [0.0] * 5
tamanho= len(notas)
soma=0
cont=0
for x in range(tamanho):
    notas[x]=float(input(f"Digite a nota do aluno {nomes[x]}: "))
for i in range(tamanho):
    soma += notas[i]
media = soma/tamanho
for y in range(tamanho):
    if notas[y]>media:
        cont=cont+1
print(f"A media da sala é {media} e {cont} alunos tem nota acima da media")

