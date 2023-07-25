import numpy as np
import pandas as pd

def activacion(x):
    if x>=0:
        return 1
    else:
        return -1

def Madaline(df_inputs,alpha,epochs):
    #Generar persos aleatorios
    weight = np.random.random((df_inputs.shape[1],df_inputs.shape[1]))
    #weight = [[0.05,0.2,0.3],[0.1,0.2,0.15]]
    bias   = np.random.random(df_inputs.shape[1])
    #bias   = []
    print(f'Pesos: {weight}')
    print(f'Bias de las {bias}')
     
    #w = np.array([0.5 for i in range(weight.shape[1])])
    w = [0.5,0.5,0.5]
    print(f'Este es el vector 3 v {w}')
    b = 0.5
    x = 0
    epochs+=1
    repetir=True
    while repetir:
        error = []
        z_input = np.zeros(bias.shape[0])
        z = np.zeros(bias.shape[0])
        print("Epocas: "+str(epochs))
        for i in range(df_inputs.shape[0]):
            for j in range(df_inputs.shape[1]):
                z_input[j] = sum(weight[j]*df_inputs[i]) + bias[j]
                z[j]= activacion(z_input[j])
 
            y_input = sum(z*w) +b
 
            y = activacion(y_input)
            clase =t[i]
            # Update the weight & bias
            if y != t[i]:
                print("Actualizar pesos")
                for j in range(weight.shape[1]):
                    weight[j]= weight[j] + alpha*(t[i]-z_input[j])*t[i][j]
                    print(weight[j])
                    bias[j]  = bias[j] + alpha*(t[i]-z_input[j])
                break
            else:
                print("Pesos finales encontrados")
                break
                

        x+=1
        if(repetir):
            repetir=False
        break
         
    return weight, bias


# Target values
x = np.array([[1.0, 1.0, 1.0], 
              [1.0, -1.0, 1.0],
              [-1.0, 1.0, 1.0],
              [-1.0, -1.0, -1.0]])

t = np.array([-1, 1, 1, -1])
 
w,b = Madaline(x, 0.5, 0)
print('weight :',w)
print('Bias :',b)