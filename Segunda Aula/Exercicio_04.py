# Receber o tipo de combustivel e calcular o valor a pagar #
litros = float(input("Quantos litros você encheu?: "))
tipo = input("Digite o tipo de combustivel: ")

if tipo == "G" and "g":
    valor = litros*5.80
    print(f"Voce precisa pagar: {valor} ")
else:
    valor = litros * 4.90
    print(f"Voce precisa pagar: {valor} ")



