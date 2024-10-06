usuario = [""]*5
senha = [""]*5 
cont = 0         

while True:
    print(f'Menu\n'
          '1 - Cadastro\n'
          '2 - Login\n'
          '3 - Mostrar Usuários\n'
          '4 - Sair')
    
    escolha = int(input("Digite a opção: "))

    if escolha == 4:
        print("Fim do Programa.")
        break 

    elif escolha == 3:
        for i in range(cont): 
            print(f'Usuário: {usuario[i]}')

    elif escolha == 2:
        login = input("Digite o login: ")
        senhas = input("Digite a senha: ")

        for i in range(cont):
            if usuario[i] == login and senha[i] == senhas:
                print(f"Login bem sucedido, {login}")
                break
        else:
            print("Login ou senha inválidos.")
        
        if i < cont and usuario[i] == login and senha[i] == senhas:
            break

    elif escolha == 1:
        login = input("Digite o login: ")
        senhas = input("Digite a senha: ")
        usuario[cont] = login
        senha[cont] = senhas
        cont += 1
    
    else:
        print('Opção inválida, tente novamente.')
