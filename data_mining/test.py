import math
datos_lista = [10,11,17,15,22,25,14,19]
rango = max(datos_lista) - min(datos_lista)

intervalos  = round(1 + (3.322 * (math.log(len(datos_lista),10))))  
amplitud = rango/intervalos
print(intervalos, amplitud)

l_inferior = []
l_superior = []

    