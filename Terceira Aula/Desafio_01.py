hora1 = int(input("digite a hora: "))
minuto1 = int(input("digite o minuto: "))
hora2 = int(input("digite a hora: "))
minuto2 = int(input("digite o minuto: "))

hora = hora1 + hora2
resto_hora  = hora % 12
hora_add = resto_hora + 1
minuto = minuto1 + minuto2
resto_minuto = minuto % 60


if minuto > 60:
  print(f"O horário final é {hora_add}:{resto_minuto}")
else:
    print(f"O horario final é {resto_hora}:{resto_minuto}")

