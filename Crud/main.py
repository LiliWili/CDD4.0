import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="turma_d"
)
cont = 0
meucursor = banco.cursor()
while True:
    print(f"1 - Cadastro\n"
          "2 - Mostrar Dados\n"
          "3 - Sair")
    escolha = int(input("Digite a opção: "))

    if escolha == 3:
        meucursor.close()
        banco.close()
        print("Fim do Programa.")
        break

    elif escolha == 2:
        for i in range(cont):
            pesquisa = 'select * from alunos;'
            meucursor.execute(pesquisa)
            resultado = meucursor.fetchall()
            for x in resultado:
                print(x)

    elif escolha == 1:
        nome1 = input("Digite o nome: ")
        telefone1 =input("Digite o telefone: ")
        sql = "insert into alunos (nome, telefone) values (%s,%s)"
        data = (nome1, telefone1)
        meucursor.execute(sql,data)
        banco.commit()
        cont += 1

    else:
        print("Opção inválida, tente novamente.")



