resposta = 1
while resposta != 2:
    alunos = int(input("Quantos alunos tem na sala?: "))
    soma = 0
    n = 0
    while n < alunos:
        notas = int(input("Digite um valor: "))
        n = n + 1
        soma = soma + notas
    media = soma/alunos
    print(f"A média aritmética da turma é: {media}")
    resposta = int(input("Deseja fazer novamente? 1 para sim 2 para não: "))