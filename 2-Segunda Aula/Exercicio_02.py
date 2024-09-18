# Receber tres notas e calcular se o aluno esta aprovado, reprovado ou em recuperação#
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
res = (nota1+nota2+nota3)/3
if res >= 7:
    print(f"Aluno aprovado com media {res}")
else:
    if res > 4:
        print(f"Aluno em recuperação com media {res}")
    else:
        print(f"Aluno reprovado com media {res}")

