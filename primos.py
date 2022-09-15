import numpy as np

m = int(input("Ingrese la dimensión de una matriz cuadrada: "))
maxi = m*m 
v = [] 
cont = 0 
for i in range(2,1000):
    primos = True 
    for j in range(2,i):
        if i == j:
            break 
        elif i%j == 0:
            primos = False 
        else: 
            continue 
    if primos == True:
        v.append(i)
        cont += 1 
        if cont == maxi:
            break 

vector = np.array(v) 
print(vector)

matriz = np.empty((m,m), int) 

pos = 0 
for i in range (0,m):
    for j in range (0,m):
        matriz[i][j] = vector[pos] 
        pos = pos + 1 


print(str(matriz).replace(' [', '').replace('[', '').replace(']', ''))

diag =[]
for i in range(m):
    for j in range(m):
        if i <= j:
            diag.append(matriz[i][j]) 

suma = sum(diag)


print("La suma de los elementos en la matriz diagonal superior es:", suma)





