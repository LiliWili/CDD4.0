#Ler um numero e dizer se ele é impar ou par e se é positivo ou negativo#
num = int(input("Digite um numero: "))
if num %2 == 0 and num > 0:
    print(f"O numero {num} é par e positivo")
elif num %2 == 0 and num < 0:
    print(f"O numero {num} é par e negativo")
elif num % 2 != 0 and num < 0:
    print(f"O numero {num} é impar e negativo")
elif num % 2 != 0 and num > 0:
    print(f"O numero {num} é par e positivo")

#Jeito do professor#
num = int(input("Digite um numero: "))
if num % 2 == 0:
    if num > 0:
        print("o numero é par e positivo")
    else:
       print("O numero  impar negativo")
    if num % 2 != 0:
        if num < 0:
            print("o numero é impar e negativo")
        else:
            print("O numero par negativo")




