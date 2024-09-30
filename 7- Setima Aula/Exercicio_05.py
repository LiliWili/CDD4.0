#Receber 5 numeros e printar de tras pra frente#
num = [0]*5
tam=len(num)
for x in range(tam):
    num[x]=int(input("Digite 5 numeros: "))
for i in range(4, -1,-1):
    print(num[i])
