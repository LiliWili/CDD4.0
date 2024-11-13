## Exemplo de manipulação de arquivo
with open("nomes.txt", "a") as arquivo:
    nome = input("Digite um nome: ")
    arquivo.write(f"{nome} \n")

def Arquivo(nome):
    while True:
        print(f"1 - Gravar\n"
              "2 - Mostrar\n"
              "3 - Sair")
        escolha = int(input("Digite a opção: "))

        if escolha == 3:
            print("Fim do Programa.")
            break

        elif escolha == 1:
            with open("nomes.txt", "a") as arquivo:
                nome = input("Digite um nome: ")
                arquivo.write(f"{nome} \n")

        elif escolha == 2:
            with open("nomes.txt", "r") as arquivo2:
                conteudo = arquivo2.read()
                print(conteudo)
        else:
            print("Opção inválida, tente novamente.")