import numpy as np
# Visualización de los estados con pygame
import pygame
import time

# ----------------------------Animación--------------------------------------------------------------------
def animacion(ENTRADA, PATRON_ASOCIADO):

    # Definir el tamaño de la ventana y del array PATRON
    ventana_ancho = 15
    ventana_alto = 15
    cellsize = 25

    # Crear la ventana
    pygame.init()
    surface = pygame.display.set_mode((ventana_ancho * cellsize, ventana_alto * cellsize))
    pygame.display.set_caption("Animación de Patrones")

    # Bucle principal
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Llenar la superficie con color
        surface.fill((211, 211, 211))

        for i in range(ventana_alto):
            for j in range(ventana_ancho):
                if ENTRADA[i, j] == -1:
                    color = (0, 0, 0)  # Negro para -1
                else:
                    color = (255, 0, 0)  # Rojo para 1

                pygame.draw.rect(surface, color, (j * cellsize, i * cellsize, cellsize, cellsize))

                # Actualizar la ventana después de dibujar cada celda
                pygame.display.update()
        time.sleep(0.5)  # Pausa de 1 segundo entre cada cambio de celda


        # Dibujar las celdas en la ventana
        for i in range(ventana_alto):
            for j in range(ventana_ancho):
                if PATRON_ASOCIADO[i, j] == -1:
                    color = (0, 0, 0)  # Negro para -1
                else:
                    color = (255, 0, 0)  # Rojo para 1

                pygame.draw.rect(surface, color, (j * cellsize, i * cellsize, cellsize, cellsize))

                # Actualizar la ventana después de dibujar cada celda
                pygame.display.update()
                time.sleep(0.1)  # Pausa de 1 segundo entre cada cambio de celda
        # Esperar a que se cierre la ventana para finalizar la animación
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
    pygame.quit()

def actualizacion(matriz2,matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    filas2 = len(matriz2)
    columnas2 = len(matriz2[0])
    res = []
    m3 = [[0 for _ in range(columnas2)] for _ in range(filas)]
    
    for i in range(filas):
        for j in range(columnas):
            multiplicacion = matriz[i][j] * matriz2[i]
            suma = np.sum(multiplicacion)

        res.append(suma)
    #print(res)
        for i in range(len(res)):
            if res[i] >= 1:
                res[i] = 1
            else:
                res[i] = -1

        for i in range(m3):
            m3[i][j]=res
    for i in m3:
        print(i, end=' ')   
        print() 


    #return res
#s=[[0,1,2],[0,2,1],[1,2,0]]
#s1=[[1,1,2],[2,0,1],[1,0,2]]
#actualizacion(s,s1)

def get_transpuesta_patron(patron1):
    t = []
    # Lo que hace internamente es es tomar cada fila de la matriz y transponerla de manera vertical (modo columna)
    for fila in patron1:
        # fila = arreglo que se desea remodelar
        # len(fila) = consiste en la longitud que va a tenir el nuevo vector transpuesto
        # 1 = cantidad de columnas
        transpuesta = np.reshape(fila, (len(fila), 1))
        t.append(transpuesta)
    return t

# Recibe el patron 1 y cada uno de los nuevos vectores transpuestos (multiplicar fila * columna)
def multiplicar_patrones(patron1, t):
    x = []
    # zip = permite iterar dos variables de igual manera
    for p, ti in zip(patron1, t):
        x_i = p * ti
        x.append(x_i)
        #print("Regla de hebb")
        #print(x_i)
    return x

def diagonal_matriz_suma(x):
    # Se suman todas las matrices de la regla de Hebb
    suma = np.sum(x, axis=0)
    # Pone en la diagonal principal de una matriz 0's
    np.fill_diagonal(suma, 0)
    print("-----Memoria de hopfield-----")
    print(suma)
    return suma

def activacion(patron1, suma):
    n = patron1.shape
    f = n[0]
    d = n[1]
    # Se crea una matriz de ceros
    l = np.zeros(shape=(len(patron1), d))
    i = 0
    # Se multiplican las columnas de memoria de hopfield * cada columna del vector distorionado
    for s in patron1:
        lista1 = []
        for k in suma:
            p_i = s * k
            #print("-----------")
            #print(p_i)
            sum = np.sum(p_i)

            lista1.append(sum)
        l[i] = lista1
        i = i + 1
    return l

def estable(patron1, l):
  # Comparar  si los valores son iguales en cada matriz
  son_iguales = np.array_equal(patron1, l)

  if son_iguales:
      print("<<<<<<<<<<Es estable>>>>>>>>>")
  else:
      print("<<<<<<<<<<No es estable: java nais dei>>>>>>")

def validar_asociacion(patron_1, patron_2):
  # Comparar  si la memoria lo recordó el patrón original
  son_iguales = np.array_equal(patron_1, patron_2)

  if son_iguales:
      print("Memoria asociada correctamente")
  else:
      print("Memoria asociada incorrectamente: java nais dei")

# Patrones de entrenamiento
patron1 = np.array([[-1,-1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                    [-1,-1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                    [-1,-1,-1, 1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1],
                    [-1,-1,1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, -1, -1],
                    [-1,1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1],
                    [-1,1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1],
                    [-1,1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1],
                    [-1,-1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1],
                    [-1,-1,-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1],
                    [-1,-1,-1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1],
                    [-1,-1,-1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1],
                    [-1,-1,-1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1],
                    [-1,-1,-1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1],
                    [-1,-1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                    [-1,-1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]])

# Patrón distorsionado
patron2 = np.array([[-1,-1,-1,-1,-1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                    [-1,-1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                    [1,1,1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, -1],
                    [-1,1,1, 1, 1, 1, -1, -1, 1, 1, 1, 1, 1, 1, -1],
                    [-1,1,1, 1, 1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1],
                    [-1,-1,1, 1, 1, 1, -1, -1, 1, 1, 1, 1, 1, -1, -1],
                    [-1,-1,-1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, -1, -1],
                    [-1,-1,-1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1],
                    [-1,-1,-1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, -1, -1],
                    [-1,-1,-1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1],
                    [-1,-1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                    [-1,-1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                    [-1,-1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                    [-1,-1,-1,-1,-1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                    [-1,-1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]])

# Transformar los patrones
t = get_transpuesta_patron(patron1)

# Multiplicar los patrones
x = multiplicar_patrones(patron1, t)

# Modificar la diagonal de la matriz resultante poniéndola en 0's
suma = diagonal_matriz_suma(x)

print("Verificar si es estable, es decir, si recuerda su patron original")
multiplicacion = activacion(patron1,suma)
# Una vez que ya se tienen los resultados de las sumas, esta función "where" lo que hace es evaluar los valores dentro de ella y dada cierta condición
# se le asignarán valores como si se pasaran por una función de activación.
nueva_matriz = np.where(multiplicacion >= 0, 1, -1)
print(nueva_matriz)
# Comparar los patrones
estable(multiplicacion, patron1)
print("Asociación")
multiplicacion2 = activacion(patron2,suma)
# Si el valor de cada punto de la matriz no cumple la condición se le asigna 1, sino, -1
nueva_matriz2 = np.where(multiplicacion2 >= 1, 1, -1)
print(nueva_matriz2)
validar_asociacion(patron1,patron2)

animacion(ENTRADA = patron2, PATRON_ASOCIADO = nueva_matriz2)
