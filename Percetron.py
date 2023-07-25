
import math
import numpy as np
import pandas as pd
from random import random
import random 
import time

start = time.time()

def generadorPesos(y: int):
    x = []
    for i in range(y):
        x.append(random.random())
    return x

# Funciones de activación
def sigmoide(x):
    y = 1 / (1+ math.exp(-x))
    return y

def tangente(x):
    y = (2 / (1 + math.exp(-2*(x))) - 1)
    return y

# Combinación lineal
          # Recibe las entradas y los pesos
def combinacion_lineal(df_inputs, df_pesos):
    combinacion = []
            # Longitud de las entradas
    for i in range(len(df_inputs)):
        # Agregar a la lista la multiplicación de las entradas por los pesos
        combinacion.append(df_inputs[i]*df_pesos[i])
    # Sumar el resultado de esas multiplicaciones en uno solo
    resultado = sum(combinacion)
    return resultado

def ajuste_de_pesos(instance, learning_rate, error, pesos):
    for i in range(len(instance)):
        # wi = wi + (alpha * error * xi)
        pesos[i] = pesos[i] + (learning_rate * error * instance[i])
    return pesos

def entrenamiento(df_inputs, pesos, epochs):
    repetir = True
    while(epochs<18):
        errorcont = 0
        epochs+=1
        print("Epocas: "+str(epochs))
        for i in range(len(df_inputs)):
            arr = df_inputs.iloc[i].to_numpy()
            combinacionL = combinacion_lineal(arr, pesos)
            #print("Instancia: "+str(arr))
            print("Combinacion lineal: "+str(combinacionL))

            # Si el error es = 0 avanzamos
            # Si es diferente de 0, se ajustan los pesos
            if combinacionL >=0:
                y = 1
            else:
                y = 0
            
            print("Activacion: "+str(y))
            error = df_Outputs[i] - y
            errorcont = error + errorcont
            print("Error: "+str(error))

            if error !=0:
                print("Ajuste de pesos: "+str(i+1))
                pesos = ajuste_de_pesos(arr,1.0,error,pesos)
                print(pesos)
                break
            if ((errorcont == 0) and (i==max(range(len(df_inputs))))):
                print("Terminado")
                repetir = False
                break

        if(epochs<17):
            print("Error")
            entrenamiento(df_inputs,pesos,epochs)
        break


# Menú
caso = 2

if (caso == 1):
    df = pd.read_csv("and.csv")
    df_Outputs = df.iloc[:,-1] # Separar la clase
    df_inputs = df.drop(df.iloc[:,-1:].columns, axis=1) # Atributos
else:
    if(caso == 2):
        df = pd.read_csv("or.csv")
        df_Outputs = df.iloc[:,-1] # Separar la clase
        df_inputs = df.drop(df.iloc[:,-1:].columns, axis=1) # Atributos
    else:
        if (caso == 3):
            df = pd.read_csv("BD2.csv")
            df_Outputs = df.iloc[:,-1] # Separar la clase
            df_inputs = df.drop(df.iloc[:,-1:].columns, axis=1) # Atributos



#Agregar el Bias
#df_inputs.insert(0,"Bias",1,allow_duplicates =False)

#Se generan pesos aleatorios
weights = generadorPesos(len(df.axes[1]))
#Pesos establecidos manualmente
pesosE = [1.5,0.5,1.5]

print("Pesos Iniciales")
print(pesosE)

entrenamiento(df_inputs,pesosE,0)
print("Pesos finales")
print(pesosE)

print("Tiempo de ejecucion:")
end = time.time()
print(end - start)