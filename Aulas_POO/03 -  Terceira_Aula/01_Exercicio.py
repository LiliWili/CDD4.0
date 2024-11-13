##Exemplos tratamento de erro

try:
    a = 4
    b = 0
    divisao = a/b
    print(divisao)
except ZeroDivisionError:
    print(f"Não podemos dividir um numero por zero")

try:
    print(x)
except NameError:
    print(f"Variavel não encontrada")