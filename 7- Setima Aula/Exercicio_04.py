A = [0]*10
tam=len(A)
M= [0]*10
X=int(input("Digite um numero: "))
for x in range(tam):
    A[x]=int(input("Digite 10 numeros: "))
for i in range(tam):
    M[i]= A[i]*X
print(M)
