#Receber o nome de dois times e os numeros de gols que cada um teve, depois dizer qual time venceu ou se foi empate#
time1 = input("Digite o nome do primeiro time: ")
time2 = input("Digite o nome do segundo time: ")
placar1 = int(input(f"Digite o numero de gols do {time1}: "))
placar2 = int(input(f"Digite o numero de gols do {time2}: "))

if placar1 == placar2:
    print("O jogo terminou empatado")
else:
    if placar1 > placar2:
        print(f"O time vencedor foi {time1}")
    else:
        print(f"O time vencedor foi {time2}")



