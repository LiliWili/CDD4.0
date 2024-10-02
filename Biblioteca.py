def piramide(num):
    for x in range(1, num+1):
        for n in range(1, x +1):
            print(x, end= " ")
        print()

def piramide_2(num):
    for x in range(1, num+1):
        for n in range(x):
            print(n+1, end= " ")
        print()

#Contar quantas vogais tem no texto#
def vogais(texto):
    tam=len(texto)
    cont=0
    for i in range(tam):
        if texto[i] == "a" or texto[i] =="e" or texto[i]=="o" or texto[i]=="i" or texto[i] == "u":
           cont+=1
    print(f"O texto tem {cont} vogais")

#Jeito do profe#

def vogais2(texto):
    cont=0
    for i in texto:
        if i in "aeiouAEIOU":
           cont+=1
    print(f"O texto tem {cont} vogais")