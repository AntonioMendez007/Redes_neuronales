import pandas as pd
import numpy as np
import random 
import math
import time

start = time.time()

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

#Función para generar pesos aleatorios
def generadorPesos(y: int):
    x = []
    for i in range(y):
        x.append(random.random())
    return x

def ajuste_de_pesos(instance, learning_rate, error, pesos):
    for i in range(len(instance)):
        # wi = wi + (alpha *(error)* xi)
        pesos[i] = pesos[i] + (learning_rate * error * instance[i])
    return pesos

def entrenamiento(df_inputs, pesos, x):
    repetir=True
    while(repetir):
        errorcont = 0
        x+=1
        print("Epocas: "+str(x))
        for i in range(len(df_inputs)):
            arr = df_inputs.iloc[i].to_numpy()
            combinacionL = combinacion_lineal(arr, pesos)
            print("Instancia: "+str(arr))
            print("Combinacion lineal: "+str(combinacionL))

            error = df_Outputs[i] - (combinacionL)
            errorCuadrado = pow(error,2)
            errorcont = errorCuadrado + errorcont
            print("Diferencia: "+str(error))
            print("Error^2: "+str(errorCuadrado))
            print(f'Suma del error^2: {errorcont}')

            print("Ajuste de pesos en la instancia: "+str(i+1)) 
            pesos = ajuste_de_pesos(arr,0.1,error,pesos)
            print(f'Pesos: {pesos}')

            if (i==max(range(len(df_inputs)))):
                if (errorcont>2):
                    print("Pesos finales encontrados")
                    break
                else:
                    print("Hubo error")
                    entrenamiento(df_inputs, pesos, x)
                    
                    break
        if(repetir):
            repetir=False
        break
 

# Menú
caso = 3

if (caso == 1):
    df = pd.read_csv("and.csv")
    df_Outputs = df.iloc[:,-1] # Separar la clase
    df_inputs = df.drop(df.iloc[:,-1:].columns, axis=1) # Atributos
else:
    if(caso == 2):
        df = pd.read_csv("orr.csv")
        df_Outputs = df.iloc[:,-1] # Separar la clase
        df_inputs = df.drop(df.iloc[:,-1:].columns, axis=1) # Atributos
    else:
        if(caso == 3):
            df = pd.read_csv("or.csv")
            df_Outputs = df.iloc[:,-1] # Separar la clase
            df_inputs = df.drop(df.iloc[:,-1:].columns, axis=1) # Atributos



#Agregar el Bias
#df_inputs.insert(0,"Bias",1,allow_duplicates =False)

#Generar pesos aleatorio
weights = generadorPesos(len(df.axes[1]))

#Pesos dados manualmente
pesosE = [0.1, 0.1, 0.1]

print("Pesos Iniciales")
print(pesosE)

entrenamiento(df_inputs,pesosE,0)
print("Pesos finales")
print(pesosE)

print("Tiempo de ejecucion:")
end = time.time()
print(end - start)