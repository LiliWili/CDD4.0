# Receber o tipo de combustivel e calcular o valor a pagar mas o codigo apenas aceita letras
# especificas e se for diferente mostrara uma mensagem de erro

litros = float(input("Quantos litros você encheu?: "))
tipo = input("Digite o tipo de combustivel: ")

if tipo == "G" or tipo == "g":
    valor = litros*5.80
    print(f"Voce precisa pagar: {valor} ")
else:
    if tipo == "E" or tipo == "e":
        valor = litros * 4.90
        print(f"Voce precisa pagar: {valor} ")
    else:
        print("Digite a letra correta")



