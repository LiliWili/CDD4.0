#Receber duas notas, somar elas e mostrar a média
nome = input("Digite o nome do aluno(a): ")
nota1 = float(input("Digite a primeira nota do aluno(a): "))
nota2 = float(input("Digite a segunda nota do aluno(a): "))
resultado = (nota1+nota2)/2
print(f"A média do aluno(a) {nome} é:{resultado}")
