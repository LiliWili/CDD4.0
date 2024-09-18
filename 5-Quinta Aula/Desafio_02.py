#Ler a senha e apos 3 tentativas sair do while informando que a senha esta bloqueada#

pin= 1234
senha = int(input("Digite sua senha: "))
tentativas = 1

while senha != pin and tentativas <3:
    senha = int(input("Digite sua senha: "))
    tentativas += 1

if tentativas == 3 and senha != pin:
    print("Senha bloqueada")
else:
    print("Login efetuado")
