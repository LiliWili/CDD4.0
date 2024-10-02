#Exemplo função#
def imprime_nome(num):
    print(f"Nome: {num}")
imprime_nome("Erickson")
imprime_nome("Renan")
imprime_nome("Daniel")

#Exercicio#
def piramide(num):
    for x in range(1, num+1):
        for n in range(1, x +1):
            print(x, end= " ")
        print()
piramide(5)
