from tkinter import Y
import pandas as pd
import numpy as np
import random 
import math
import time

start = time.time()

def numeroEntradas(df):
    entradas = len(df.axes[0]) #Calcular el numero de Instancias
    return entradas

def numeroSalidas(df):
    salidas = len(df.value_counts()) #Calcular el numero de salidas
    return salidas

def generadorPesos(y: int):
    x = []
    for i in range(y):
        x.append(random.random())
    return x

def media_normalizacion(df): #La normalización se hace restando la media y dividiendo por la desviación estándar para todos los elementos del Dataframe.#
    return df.apply(lambda x: (x-x.mean())/ x.std(), axis=0)

def minmax_normalizacion(df): #El resultado de la normalización resta el valor mínimo de Dataframe y lo divide por la diferencia entre el valor más alto y el más bajo de la columna correspondiente.#
    return (df - df.min()) / ( df.max() - df.min())

def conversionCategorica(df):
    a = np.unique(df) #Con np.unique obtengo los valores unicos que no se repiten
    #Aqui lo que yo tenia pensado era que, por cada valor de la clase comparar, 
    #si el valor en i es igual al valor que tenemos en a en la posicion j, 
    # remplazo lo que tengo en el df en la posicion i por el numero que es j
    #ejemplo: 
    #print(a[0])
    #print((df_Outputs[0]))
    #vemos que es el mismo valor, entonces hacemos la condicion
    #print( (df_Outputs[0]) == (a[0])) 
    for i in (range(len(df))): #A ver aqui tuve que poner range(len()) porque si no, no jala
        for j in range(len(a)):
            if ((df[i]) == (a[j])):
                df= df.replace(df[i],j) #Reemplazo en todo el dataframe el valor viejito por el nuevo, luego lo convierto en funcion u.u, pa que vea mis comentarios todos mensos
    return df

def sigmoid(x):
    y = 1 / (1 + math.exp(-x))
    return y

def tangencial(x):
    y = (1 - math.exp(-2*x))/(1 + math.exp(-2*x))
    return y

def combinacion_lineal(df_inputs, df_weights):
    comb = []
    for i in range(len(df_inputs)):
        comb.append(df_inputs[i] * df_weights[i])
    res = sum(comb)
    return res
'''
def ajustes_Peso(pesos, cambios):
    for i in range(len(pesos)):
        pesos[i] = pesos[i] + cambios[i]
    return pesos

def cambio(taza_aprendizaje, diferencia, instancia):
    cambios = list()
    for i in range(len(instancia)):
        cambios.append(taza_aprendizaje * diferencia * instancia[i])
    return cambios
'''
def ajuste_de_pesos(instance, learning_rate, error, pesos):
    for i in range(len(instance)):
        # wi = wi + (alpha *(error)* xi)
        pesos[i] = pesos[i] + (learning_rate * error * instance[i])
    return pesos

def entrenamiento(df_Inputs, pesos, lms,x):
    repetir = True
    while(repetir):
        errorcont = 100
        x = x + 1
        print("Epoca: "+str(x))
        for i in range(len(df_Inputs)):
            #print(i)
            arr = df_Inputs.iloc[i].to_numpy()
            combinacionL = combinacion_lineal(arr, pesos)
            print("Instancia: "+str(arr))
            print("Combinacion lineal: "+str(combinacionL))

            error = df_Outputs[i] - (combinacionL)
            print("Diferencia: "+str(error))

            LMS = pow(error,2)
            errorcont = LMS + errorcont

            print("Error^2: "+str(LMS))
            print(f'Suma del error^2: {errorcont}')
            #print((errorcont == 0) and (i==max(range(len(df_Inputs)))))
            print('-----')
            print("AJUSTE DE PESOS EN LA INSTANCIA: "+str(i+1)) 
            pesos = ajuste_de_pesos(arr,0.1,error,pesos)
            print('Pesos nuevos')
            print(pesos)
            if (i==max(range(len(df_Inputs)))):
                if (errorcont>lms):
                    print("PESOS FINALES ENCONTRADOS") 
                    break
                else:
                    print("Hubo error")
                    entrenamiento(df_Inputs, pesos, lms,0)
                    break
        if(repetir):
            repetir=False
        break
caso = 3

if (caso == 1):
    df = pd.read_csv("orr.csv")
    #df = df.drop(['Id'], axis=1) #Aqui quitamos el ID porque no nos sirve
    df_Outputs = df.iloc[:, -1] #Separo la clase de los atributos
    df_Inputs = df.drop(df.iloc[:, -1:].columns, axis=1) #Aqui estan los puros atributos
else: 
    if (caso == 2):
        df = pd.read_csv("and.csv")
        #df = df.drop(['Id'], axis=1) #Aqui quitamos el ID porque no nos sirve
        df_Outputs = df.iloc[:, -1] #Separo la clase de los atributos
        df_Inputs = df.drop(df.iloc[:, -1:].columns, axis=1) #Aqui estan los puros atributos
    else:
        if (caso == 3):
            df = pd.read_csv("or.csv")
            #df = df.drop(['Id'], axis=1) #Aqui quitamos el ID porque no nos sirve
            df_Outputs = df.iloc[:, -1] #Separo la clase de los atributos
            df_Inputs = df.drop(df.iloc[:, -1:].columns, axis=1) #Aqui estan los puros atributos

#Inserto el BIAS
#df_Inputs.insert(0, "BIAS", 1, allow_duplicates=False)

N_Input = numeroEntradas(df_Inputs)
N_Output = numeroSalidas(df_Outputs)
weights = [0.1,0.1,0.1] #generadorPesos(len(df.axes[1]))


print("Pesos Iniciales")
print(weights)

#print(df_Inputs)
#print(df_Outputs)

                          
entrenamiento(df_Inputs, weights,1, 0)
print("Pesos Finales")
print(weights)

print("Tiempo de ejecucion:")
end = time.time()
print(end - start)