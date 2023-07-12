import pandas as pd
import openpyxl
import matplotlib as ptl

##acceso al documento
doc= openpyxl.load_workbook("Estaturas.xlsx")
##acceso a la hoja
hoja = doc.get_sheet_by_name("Hoja1")
p = []

##EXTRACCIÓN DE DATOS 
for row in hoja.iter_rows():
    pesos = row[0].value
    p.append(pesos)
datos_lista = [] 
## QUITAR PRIMER DATO DE LA COLUMNA
for x in range(1,len(p)):
    datos_lista.append(p[x])

##DEFINIR RANGO , INTERVALOS Y AMPLITUD
rango = max(datos_lista) - min(datos_lista)

inter = int(input('cuantas clasificaciones quieres?\t \n'))


#intervalos  = round(1 + (3.322 * (math.log(len(datos_lista),10))))  
amplitud = rango/inter
print(min(datos_lista), ' \n ---------')

incremento = min(datos_lista)
clasi= []
clasi_name = []


for x in range(inter):

    listing = 0
    for y in datos_lista:
        if y >= incremento and y <(round(incremento + amplitud,2) ):
            listing=listing + 1
        else:
            False

    clasi.append(listing)
    clasi_name.append((round(incremento,2),'-',round(incremento + amplitud,2)))
    incremento= round(incremento + amplitud,2)
    print(incremento)

dframe= {


    'Cantidad':clasi,
    'Clasificacion':clasi_name

}

df = pd.DataFrame(dframe)
print(df)



