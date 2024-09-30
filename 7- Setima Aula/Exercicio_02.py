#Receber 5 nomes de alunos e mostrar a posicao de cada nome#
nomes = ["","","","",""]
tamanho= len(nomes)
for x in range(tamanho):
    nomes[x]=input("Digite o nome de cinco alunos: ")
for i in range(tamanho):
    print([i], nomes[i],end=" ")
