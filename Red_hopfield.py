import numpy as np
import math

def patron1(m,fila,columna):
    # Creamos una matriz de ceros para ir almacenando los demás valores
    h = [[0 for _ in range(columna)] for _ in range(fila)]
    # Recorrer la matriz y realizar la multiplicación
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i!=j:
                h[i][j] = m[i][j] * i * j
            else:
                h[i][j] = 0
    for i in h:
        print(i, end=' ')   
        print()
    return h

def x_1(m,fila,columna):
    # Creamos una matriz de ceros para ir almacenando los demás valores
    m3 = [[0 for _ in range(columna)] for _ in range(fila)]

    # llenar matriz
    for i in range(fila):
        for j in range(columna):
            # Sin el indice/numero de la fila el diferente que el de la columna, se realiza la miltiplicación
            if i != j:
                m3[i][j] = m[i] * m[j]
            # si no, la coincidencia (diagonal) no se toma en cuenta
            else:
                m3[i][j] = 0

    for i in m3:
        print(i, end=' ')   
        print()

    return m3

def x_2(m2,fila,columna):
    # Creamos una matriz de ceros para ir almacenando los demás valores
    m1 = [[0 for _ in range(columna)] for _ in range(fila)]

    # llenar matriz
    for i in range(fila):
        for j in range(columna):
            # Sin el indice/numero de la fila el diferente que el de la columna, se realiza la miltiplicación
            if i != j:
                m1[i][j] = m2[i] * m2[j]
            # si no, la coincidencia (diagonal) no se toma en cuenta
            else:
                m1[i][j] = 0

    for i in m1:
        print(i, end=' ')   
        print()

    return m1

def suma(m1,m2):
    fil1=len(m1)
    col1=len(m1[0])

    fil2=len(m2)
    col2=len(m2[0])
    # Creamos una matriz de ceros para ir almacenando los demás valores
    sum = [[0 for _ in range(len(m1))] for _ in range(len(m2))]

    for i in range(fil1):
        for j in range(col2):
             if i!=j:
                sum[i][j] += m1[i][j] + m2[i][j]
             else:
                 sum[i][j]=0

    print("Memoria de hopfield")
    for i in sum:
        print(i, end=' ')   
        print()
    
    return sum

import numpy as np

def activacion(z):
    if z>=0:
        return 1 
    else:
        return -1

def patron_distorsionado(vector, matriz):
    # Crear una lista para almacenar los resultados
    resultados = []
    acti = []
    # Multiplicar el vector por cada columna de la matriz, sumar los resultados y almacenarlos en la lista
    for i in range(matriz.shape[1]):
        resultado_columna = np.sum(vector * matriz[:, i])
        act = activacion(resultado_columna)
        resultados.append(resultado_columna)
        acti.append(act)

    return acti
    

x1=[1,-1,1,-1,1,-1,1,-1]
x2=[1,1,1,1,-1,-1,-1,-1]

# Definir el vector distorsionado
vector = np.array([-1,1,1,1,-1,-1,-1,-1])

matriz1 = x_1(x1,8,8)
print("-----------------")
print("\n")
matriz2 = x_2(x2,8,8)
print("-----------------")
print("\n")

s = suma(matriz1,matriz2)
print("Matriz nueva")
matriz_nueva=np.array(s)
print(matriz_nueva)
print("\nMemoria recordada")
patron = patron_distorsionado(vector,matriz_nueva)
print(patron)

def transpuesta(m):
    transp=[]
    for i in range(len(m[0])):
        fila=[]
        for j in range(len(m)):
            fila.append(m[j][i])
        transp.append(fila)
    
    print("\nTranspuesta")
    for i in transp:
        print(i, end=' ')   
        print() 

def multiplicacion(m1,m2):
    fil1=m1
    col1=m1[0]

    fil2=len(m2)
    col2=len(m2[0])

    if len(col1)==fil2:
        print("Se puede multiplicar")
        # Creamos una matriz de resultado con valores 0
        m3 = [[0 for _ in range(col2)] for _ in range(fil1)]
        
        for i in range(len(fil1)):
            for j in range(col2):
                for k in range(fil2):
                    m3[i][j] += m1[i][k] * m2[k][j]

        print("\nMultiplicacion")
        for i in m3:
            print(i, end=' ')   
            print() 
    else:
        print("No se puede multiplicar")
    return m3

matriz =np.array([[-1,-1,-1, 1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1],
        [-1,-1,1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, -1, -1],
        [-1,1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1],
        [-1,1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1],
        [-1,1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1],
        [-1,-1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1],
        [-1,-1,-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1],
        [-1,-1,-1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1],
        [-1,-1,-1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1],
        [-1,-1,-1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1],
        [-1,-1,-1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1]])
print("\n")
transpuesta = np.transpose(matriz)
print(transpuesta)
print("\n")
multiplica = np.dot(matriz,transpuesta)
print(multiplica)



