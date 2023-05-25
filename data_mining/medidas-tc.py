import openpyxl
import math
##acceso al documento
doc= openpyxl.load_workbook("pesos.xlsx")
##acceso a la hoja
hoja = doc.get_sheet_by_name("Hoja1")
p = []

##EXTRACCIÓN DE DATOS 
for row in hoja.iter_rows():
    pesos = row[0].value
    p.append(pesos)
data = [] 
## QUITAR PRIMER DATO DE LA COLUMNA
for x in range(1,len(p)):
    data.append(p[x])

print(data)
if len(data)< 20:
    ## CALCULO DE MODA
    max_valor = 2
    moda = []
    for x in range (len(data)):
        counter = 0 
        for i in range(len(data)):
            if data[x] == data[i]:
                counter = counter + 1
        if  counter >= max_valor:
            max_valor = counter
            if counter == max_valor and (data[x] not in moda):
                moda.append(data[x])
                 
    

    ##CALCULO DE MEDIANA

    suma = 0
    for i in range(len(data)):
        suma = suma + data[i]
    
    mediana = suma / len(data)
    
    desv = 0
    for r in range(len(data)):
        desv = desv + (((data[r] - mediana)**2) / (len(data) -1))
    

    print('VARIANZA: \t',math.sqrt(desv))
    print('MODA(S) : ', moda)
    print('MEDIA:\t', mediana)

    data_sort = sorted(data)
    if len(data)%2 == 0:
        position = len(data)/ 2 
        value = (data_sort[int(position-1)] + data_sort[int(position)]) / 2
        print('MEDINA :\t', value) 
    else:
        position= ((len(data)+1) / 2) +1
        print('MEDIANA:\t', data_sort[int(position)])

else:
    print('excede la cantidad de datos requeridos')
