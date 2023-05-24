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

    y = 0
    counter = 0
    ## CALCULO DE MODA
    results = [0,0]
    while y < len(data):
        for x in range(len(data)):
            if data[y] == data[x]:
                
                counter = counter + 1 
        if counter > 1:
            if counter > results[1]:
                results[0], results[1] = data[y],counter
            elif counter == results[1] and data[y]!=results[0]:
                print('MULTIMODAL CON: \t', data[y])
                break
        
        
        


        counter = 0
        y = y + 1
    

    ##CALCULO DE MEDIANA

    suma = 0
    for i in range(len(data)):
        suma = suma + data[i]
    
    mediana = suma / len(data)
    
    desv = 0
    for r in range(len(data)):
        desv = desv + (((data[r] - mediana)**2) / (len(data) -1))
    

    print('VARIANZA: \t',math.sqrt(desv))
    print('MODA:\t', results[0])
    print('MEDIA:\t', mediana)

    if len(data)%2 == 0:
        position = len(data)/ 2 
        data_sort = sorted(data)
        print(data_sort)
        value = (data_sort[int(position)] + data_sort[int(position) + 1]) / 2
        print('MEDINA :\t', value) 
    else:
        position= ((len(data)+1) / 2) +1
        data_sort= sorted(data)
        print(data_sort)
        print('MEDIANA:\t', data_sort[int(position)])


else:
    print('excede la cantidad de datos requeridos')
