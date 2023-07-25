import numpy as np
import pandas as pd
import random
 
def activacion(z):
    if z>=0:
        return 1 
    else:
        return -1
 
def generadorPesos(y: int):
    x = []
    for i in range(y):
        x.append(random.random())
    return x

def combinacion_lineal(df_inputs, df_pesos):
    combinacion = []
            # Longitud de las entradas
    for i in range(len(df_inputs)):
        # Agregar a la lista la multiplicación de las entradas por los pesos
        combinacion.append(df_inputs[i]*df_pesos[i])
    # Sumar el resultado de esas multiplicaciones en uno solo
    resultado = sum(combinacion)
    return resultado

def combinacion_lineal2(df_inputs, df_pesos,b):
    combinacion = []
            # Longitud de las entradas
    for i in range(len(df_inputs)):
        # Agregar a la lista la multiplicación de las entradas por los pesos
        combinacion.append((df_inputs[i]*df_pesos[i]))
    # Sumar el resultado de esas multiplicaciones en uno solo
    resultado = sum(combinacion)+b
    return resultado

def ajuste_de_pesos( learning_rate, dif, pesos,df_inputs):
    for i in range(len(pesos)):
        # wi = wi + (alpha * f_netZi* diferencia)        dif (T - netzi)
        pesos[i] = pesos[i] + (learning_rate  * (dif))*(df_inputs[i])
        
    return pesos
'''
def ajuste_de_bias(bias,learning_rate, dif):
    for i in range(len(bias)):
        # wi = wi + (alpha * f_netZi* diferencia)
        bias[i] = bias[i] + (learning_rate * dif)
    return bias
'''
def ajuste_de_bias(bias,learning_rate, dif):
    
    # wi = wi + (alpha * f_netZi* diferencia)
    bias = bias + (learning_rate * dif)
    return bias
def Madaline(df_inputs, df_outputs, w1,w2,b,v):
    repetir=True
    while(repetir):
        epochs=+1
        errorC=0
        
        print(f'Epoca: {epochs}')

        for i in range(len(df_inputs)):
            # arreglo de la instancia
            inst = df_inputs.iloc[i].to_numpy()

            netZ_1=combinacion_lineal2(inst,w1,b[0])
            netZ_2=combinacion_lineal2(inst,w2,b[1])

            print("Instancia: "+str(inst))
            print("Net_Z_1: "+str(netZ_1))
            print("Net_Z_2: "+str(netZ_2))

            #print("---------------Evaluar en la Función de activación------------------")
            fnet_Z1=activacion(netZ_1)
            fnet_Z2=activacion(netZ_2)
            print(f'fnet_Z1: {fnet_Z1}')
            print(f'fnet_Z2: {fnet_Z2}')
            print("-------------Calcular net y evaluar la unidad de salida------------------")
            net_Y=v[2]+( (fnet_Z1*v[0]) + (fnet_Z2*v[1]) )
            fnet_y=activacion(net_Y)
            print(f'net_y: {net_Y}')
            print(f'fnet_y: {fnet_y}')

            dif= df_outputs[i] - netZ_1
            dif2= df_outputs[i] - netZ_2
            
            if (fnet_y != df_outputs[i]):
                errorC=errorC+1

                print("Actualizar el bias y los pesos en la instancia "+str(i+1))
                
                b[0]=(ajuste_de_bias(b[0],0.5,dif))
                b[1]=(ajuste_de_bias(b[1],0.5,dif2))

                w1=ajuste_de_pesos(0.5,dif,w1,inst)
                w2=ajuste_de_pesos(0.5,dif2,w2,inst)

            if (i==max(range(len(df_inputs)))):
                if(errorC==0):
                    print("Pesos finales encontrados")
                    repetir=False
                    break
                else:
                    print("Hubo error")
                    Madaline(df_inputs,df_outputs,w1,w1,b,v)
                    repetir=False
                    break
        

        
        




# Menú
caso = 1

if (caso == 1):
    df = pd.read_csv("xor.csv")
    df_outputs = df.iloc[:,-1] # Separar la clase
    df_inputs = df.drop(df.iloc[:,-1:].columns, axis=1) # Atributos

w1=[0.05,0.2]
w2=[0.1,0.2]
b=[0.3,0.15]
v=[0.5,0.5,0.5]

Madaline(df_inputs,df_outputs,w1,w2,b,v)

print("Pesos y bias finales")
print(w1)
print(w2)
print(b)