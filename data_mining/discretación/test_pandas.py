import pandas as pd
import openpyxl
import matplotlib.pyplot as ptl

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

inter = int(input('cuantas clasificaciones quieres?\t \n'))


estru = {
    'info':datos_lista
}

# Crear un DataFrame de ejemplo
data = pd.DataFrame(estru)

# Discretizar la columna 'A' en dos categorías con precisión decimal de 1
result= pd.cut(estru['info'], inter )
conteo = result.value_counts()

indices = []
for a in range(inter):
    indices.append(a)


ptl.bar(indices,conteo , color = "black" )
ptl.title('CONTEOS')

ptl.show()
