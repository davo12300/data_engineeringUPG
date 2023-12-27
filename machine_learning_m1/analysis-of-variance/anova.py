import random
import pandas as pd
from scipy.stats import f
import scipy.stats as stats

test_array = []

y = int(input("FILAS: "))
x = int(input("COLUMNAS: "))

for i in range(x):
    test_array.append([])
for f in range(x):
    print('RELLENANDO COLUMNA----- ',f)  
    for u in range(y): 
        
        dato= int(input('VALOR DE COLUMNA:\t'))       
        test_array[f].append(dato)



coleccion = test_array

##FUNCIONES

def promedio(arreglo):
    cal = 0
    for x in range(len(arreglo)):
        cal = cal + arreglo[x]    
    return (cal/len(arreglo))

def sumador(arreglo):
    suma = 0
    for z in range(len(arreglo)):
        suma = suma + float(arreglo[z])

    return round(suma,2)

def x_p(coleccion):
    suma = 0
    for x in range(len(coleccion)):
        suma = suma + promedio(coleccion[x])
    return(suma/len(coleccion))

def cal_cst(n,m):
    return round((n-m)**2,2)

def cal_sctr(n,m):
    return round(4 * ((n-m)**2),2)


n = len(coleccion) * len(coleccion[0])
x_promedio = x_p(coleccion)




## CALCULO SCT 

def calculate(a,b,var, colected,funcion):

    sct_array = []
    for i in range(a):        
        sct_array.append([])
    for f in range(a): 
        suma = 0       
        for u in range(b):
            if type(var) == list:
                value = funcion(colected[f][u],var[f])
            else:
                value = funcion(colected[f][u],var)
            suma = suma + value
            sct_array[f].append(value)
                    
        sct_array[f].append(round(suma,2))

    sct_array.append([])
    for f in range(b):
        cal= 0
        for p in range(a):
            cal= cal + float(sct_array[p][f])
        
        sct_array[-1].append(round(cal,2))
    
    return sct_array,sumador(sct_array[-1])
 
n_colection,n_calx = calculate(x,y,x_promedio,coleccion,cal_cst)

array_sctr = []
array_sce =[]
for j in range(len(coleccion)):
    array_sctr.append(cal_sctr(promedio(coleccion[j]),x_promedio))
    array_sce.append(promedio(coleccion[j]))

n_sctr = sumador(array_sctr)

f_colection,sce_cal = calculate(x,y,array_sce,coleccion,cal_cst)


##CALCULOS FINALES

cmt = round(n_calx / (n -1) ,2)
cmtr = round(n_sctr / (len(coleccion)-1),2)
cme = round(sce_cal / (n - len(coleccion)),2)

s = round(cmtr / cme ,2)

print('IMPRESION DE SCT')
n_colection[-1].append(n_calx)
# Determina la cantidad de columnas
num_columnas = len(n_colection)

# Determina la cantidad de filas (basado en la longitud de una de las columnas)
num_filas = len(n_colection[0])

# Imprimir la tabla
for fila in range(num_filas):
    for columna in range(num_columnas):
        print(n_colection[columna][fila], end="\t")  # Usar "\t" para separar las columnas
    print()  # Nueva línea después de cada fila


print('SUMA DE CUADRADOS TOTALES (SCT)',n_calx)
print('SUMA DE CUADRADOS DE GRUPOS (SCTR)',sumador(array_sctr))
print('SUMA DE CUADRADOS ERROR(SCE)',sce_cal)
print(
    'CMT:\t ',cmt,'\n'
    'CMTR:\t ',cmtr,'\n'
    'CME:\t ',cme,'\n'
    'S:\t ',s,'\n'
)

gl_f , gl_c= int(len(coleccion) - 1 ), int(n-len(coleccion))

f = stats.f(dfn=gl_f, dfd=gl_c)

# Calcular el valor crítico para un nivel de significancia de 0.05
valor_critico = f.ppf(1 - 0.05)

print("Valor crítico:", valor_critico)

if s > valor_critico:
    print('HIPOTESIS NULA RECHAZADA (H0)  ')
else:
    print('HIPOTESIS ALTERNATIVA VALIDA (H1): \n '
          
          'Hay diferencias significativas entre al menos dos de las medias de los grupos.'      
          
          )


##impresion de dataframe
df = pd.DataFrame(n_colection).transpose()
