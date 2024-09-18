peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso/(altura)**2
if imc <= 18.5:
    print(f"O seu imc é:{imc} vocé esta abaixo do peso melhore")
elif imc == 18.6 and imc < 24.9:
    print(f"O seu imc é:{imc} vocé esta no peso ideal parabéns")
elif imc == 25.0 and imc < 29.9:
    print(f"O seu imc é:{imc} vocé esta levemente a cima do peso")
elif imc == 30.0 and imc < 34.9:
    print(f"O seu imc é:{imc} vocé esta na obesidade grau 1")
elif imc == 35 and imc < 39.9:
    print(f"O seu imc é:{imc} vocé esta na obesidade grau 2 (severa)")
elif imc >= 40:
    print(f"O seu imc é:{imc} vocé esta na obesidade grau 3 (morbida)")
