mport openpyxl
import pandas as pd 
import matplotlib.pyplot as ptl
from collections import Counter

##acceso al documento
doc= openpyxl.load_workbook("salarios.xlsx")
##acceso a la hoja
hoja = doc.get_sheet_by_name("Hoja1")
p = []

##EXTRACCIÓN DE DATOS 
for row in hoja.iter_rows():
    pesos = row[0].value
    p.append(pesos.upper())

data = [] 
## QUITAR PRIMER DATO DE LA COLUMNA
for x in range(1,len(p)):
    data.append(p[x])


#Palabras_correctas = ['WALMART', 'WALDOS','CHEDRAUI','AURRERA','SORIANA','COMERCIAL MEXICANA']
Palabras_correctas = ['AURRERA']

for x in Palabras_correctas:

    correct = Counter(x)

    for y in data:

        check = Counter(y)
        
        verify = correct & check
        print(x,'==',y)
        
        result = (len(x) - len(y))
        
        print(verify)
        print('calculo:',result,'longitud de verify',len(verify))
        if len(verify) == result:
            print('CHEKED')
            

        result= 0

        print('i miss you')




    print('say my name')






