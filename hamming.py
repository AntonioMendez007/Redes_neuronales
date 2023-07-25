import numpy as np
import math
# Multiplicar matrices
def multiplicacion(m1,m2):
    fil1=len(m1)
    col1=len(m1[0])

    fil2=len(m2)
    col2=len(m2[0])

    if col1==fil2:
        print("Se puede multiplicar")
        # Creamos una matriz de resultado con valores 0
        m3 = [[0 for _ in range(col2)] for _ in range(fil1)]
        
        for i in range(fil1):
            for j in range(col2):
                for k in range(fil2):
                    m3[i][j] += m1[i][k] * m2[k][j]
        print(m3[0])
        print("\nMultiplicacion")
        for i in m3:
            print(i, end=' ')   
            print() 
    else:
        print("No se puede multiplicar")
    return m3
def transpuesta(m):
    transp=[]
    for i in range(len(m[0])):
        fila=[]
        for j in range(len(m)):
            fila.append(m[j][i])
        transp.append(fila)
    
    #print("\nTranspuesta")
    for i in transp:
        print(i, end=' ')   
        print()
    return transp

def red_hamming(p1,p2,p3,p4,p5,p6,w1,w2,w3):
    #combinar el vector de pesos
    w_peso = np.concatenate((w1,w2,w3) ,axis = 1)
    w = transpuesta(w_peso) 
    print(w)
    for i in range(1):
        print("Iteración número:", i+1)
        #p1
        a=multiplicacion(w,p1)
        print("p1")
        if (a[0]>a[1] and a[0]>a[2]):
            
            print("Primer neurona activada")
            alpha=0.5
            w1_new= w1 + (alpha*(np.subtract(p1, w1)))
            print("w1_new:")
            print(w1_new)
            w1=w1_new
            w_peso = np.concatenate((w1,w2,w3) ,axis = 1)
            w = transpuesta(w_peso) 
        elif(a[1]>a[0] and a[1]>a[2]):
            print("Segunda neurona activada")
            alpha=0.5
            w2_new= w2 + (alpha*(np.subtract(p1, w2)))
            print("w2_new:")
            print(w2_new)
            w2=w2_new
            w_peso = np.concatenate((w1,w2,w3) ,axis = 1)
            w = transpuesta(w_peso) 
        elif(a[2]>a[0] and a[2]>a[1]):
            print("Tercer neurona activada")
            alpha=0.5
            w3_new= w3 + (alpha*(np.subtract(p1, w3)))
            print("w2_new:")
            print(w3_new)
            w3=w3_new
            w_peso = np.concatenate((w1,w2,w3) ,axis = 1)
            w = transpuesta(w_peso)
        print("-----------------------------------")
        print("p2")
        a2=multiplicacion(w,p2)
        #p2
        if (a2[0]>a2[1] and a2[0]>a2[2]):
            print("Primer neurona activada")
            alpha=0.5
            w1_new= w1 + (alpha*(np.subtract(p2, w1)))
            print("w2_new:")
            print(w1_new)
            w1=w1_new
            w_peso = np.concatenate((w1,w2,w3) ,axis = 1)
            w = transpuesta(w_peso)
        elif(a2[0]<a2[1] and a2[1]>a2[2]):
            print("Segunda neurona activada")
            alpha=0.5
            w2_new= w2 + (alpha*(np.subtract(p2, w2)))
            print("w2_new:")
            print(w2_new)
            w2=w2_new
            w_peso = np.concatenate((w1,w2,w3) ,axis = 1)
            w = transpuesta(w_peso)
        elif(a2[0]<a2[2] and a2[1]<a2[2]):
            print("Tercer neurona activada")
            alpha=0.5
            w3_new= w3 + (alpha*(np.subtract(p2, w3)))
            print("w2_new:")
            print(w3_new)
            w3=w3_new
            w_peso = np.concatenate((w1,w2,w3) ,axis = 1)
            w = transpuesta(w_peso)
        print("-----------------------------------")
        print("p3")
        a3=multiplicacion(w,p3)
        #p3
        if (a3[0]>a3[1] and a3[0]>a3[2]):
            print("Primer neurona activada")
            alpha=0.5
            w1_new= w1 + (alpha*(np.subtract(p3, w1)))
            print("w2_new:")
            print(w1_new)
            w1=w1_new
            w_peso = np.concatenate((w1,w2,w3) ,axis = 1)
            w = transpuesta(w_peso)
        elif(a3[0]<a3[1] and a3[1]>a3[2]):
            print("Segunda neurona activada")
            alpha=0.5
            w2_new= w2 + (alpha*(np.subtract(p3, w2)))
            print("w2_new:")
            print(w2_new)
            w2=w2_new
            w_peso = np.concatenate((w1,w2,w3) ,axis = 1)
            w = transpuesta(w_peso)
        elif(a3[0]<a3[2] and a3[1]<a3[2]):
            print("Tercer neurona activada")
            alpha=0.5
            w3_new= w3 + (alpha*(np.subtract(p3, w3)))
            print("w2_new:")
            print(w3_new)
            w3=w3_new
            w_peso = np.concatenate((w1,w2,w3) ,axis = 1)
            w = transpuesta(w_peso)
        print("-----------------------------------")
        print("p4")
        a4=multiplicacion(w,p4)
        if (a4[0]>a4[1] and a4[0]>a4[2]):
            print("Primer neurona activada")
            alpha=0.5
            w1_new= w1 + (alpha*(np.subtract(p4, w1)))
            print("w2_new:")
            print(w1_new)
            w1=w1_new
            w_peso = np.concatenate((w1,w2,w3) ,axis = 1)
            w = transpuesta(w_peso)
        elif(a4[0]<a4[1] and a4[1]>a4[2]):
            print("Segunda neurona activada")
            alpha=0.5
            w2_new= w2 + (alpha*(np.subtract(p4, w2)))
            print("w2_new:")
            print(w2_new)
            w2=w2_new
            w_peso = np.concatenate((w1,w2,w3) ,axis = 1)
            w = transpuesta(w_peso)
        elif(a4[0]<a4[2] and a4[1]<a4[2]):
            print("Tercer neurona activada")
            alpha=0.5
            w3_new= w3 + (alpha*(np.subtract(p4, w3)))
            print("w2_new:")
            print(w3_new)
            w3=w3_new
            w_peso = np.concatenate((w1,w2,w3) ,axis = 1)
            w = transpuesta(w_peso)
        print("-----------------------------------")
        print("p5")
        a5=multiplicacion(w,p5)
        if (a5[0]>a5[1] and a5[0]>a5[2]):
            print("Primer neurona activada")
            alpha=0.5
            w1_new= w1 + (alpha*(np.subtract(p5, w1)))
            print("w2_new:")
            print(w1_new)
            w1=w1_new
            w_peso = np.concatenate((w1,w2,w3) ,axis = 1)
            w = transpuesta(w_peso)
        elif(a5[0]<a5[1] and a5[1]>a5[2]):
            print("Segunda neurona activada")
            alpha=0.5
            w2_new= w2 + (alpha*(np.subtract(p5, w2)))
            print("w2_new:")
            print(w2_new)
            w2=w2_new
            w_peso = np.concatenate((w1,w2,w3) ,axis = 1)
            w = transpuesta(w_peso)
        elif(a5[0]<a5[2] and a5[1]<a5[2]):
            print("Tercer neurona activada")
            alpha=0.5
            w3_new= w3 + (alpha*(np.subtract(p5, w3)))
            print("w2_new:")
            print(w3_new)
            w3=w3_new
            w_peso = np.concatenate((w1,w2,w3) ,axis = 1)
            w = transpuesta(w_peso)
        print("-----------------------------------")
        print("p6")
        a6=multiplicacion(w,p6)
        if (a6[0]>a6[1] and a6[0]>a6[2]):
            print("Primer neurona activada")
            alpha=0.5
            w1_new= w1 + (alpha*(np.subtract(p6, w1)))
            print("w2_new:")
            print(w1_new)
            w1=w1_new
            w_peso = np.concatenate((w1,w2,w3) ,axis = 1)
            w = transpuesta(w_peso)
        elif(a6[0]<a6[1] and a6[1]>a6[2]):
            print("Segunda neurona activada")
            alpha=0.5
            w2_new= w2 + (alpha*(np.subtract(p6, w2)))
            print("w2_new:")
            print(w2_new)
            w2=w2_new
            w_peso = np.concatenate((w1,w2,w3) ,axis = 1)
            w = transpuesta(w_peso)
        elif(a6[0]<a6[2] and a6[1]<a6[2]):
            print("Tercer neurona activada")
            alpha=0.5
            w3_new= w3 + (alpha*(np.subtract(p6, w3)))
            print("w2_new:")
            print(w3_new)
            w3=w3_new
            w_peso = np.concatenate((w1,w2,w3) ,axis = 1)
            w = transpuesta(w_peso)
        print("-----------------------------------")
    w = np.concatenate((w1,w2,w3) ,axis = 1)
    print("Pesos resultantes")
    w = transpuesta(w) 
    #print(w)
      
p_1=[[-0.1961],
    [0.9806]]
p_2=[[0.1961],
    [0.9806]]
p_3=[[0.9806],
    [0.1961]]
p_4=[[0.9806],
    [-0.1961]]
p_5=[[-0.5812],
    [-0.8137]]
p_6=[[-0.8137],
    [-0.5812]]

w_1=[[0.7071],
    [-0.7071]]

w_2=[[0.7071],
    [0.7071]]

w_3=[[-1.0],
    [0.0]]

h=red_hamming(p_1,p_2,p_3,p_4,p_5,p_6,w_1,w_2,w_3)
print(h)
