import openpyxl
import pandas as pd 
import matplotlib.pyplot as ptl


##acceso al documento
doc= openpyxl.load_workbook("destinos.xlsx")
##acceso a la hoja
hoja = doc.get_sheet_by_name("Hoja1")
p = []

##EXTRACCIÓN DE DATOS 
for row in hoja.iter_rows():
    pesos = row[0].value
    p.append(pesos)

upperdata = []
for z in range(len(p)):
    upperdata.append(p[z].upper())


destino, cantidad = [],[]
for y in upperdata:
    counter= 0
    for i in upperdata:
        if i == y:
            counter= counter + 1   
    if counter > 0 and y not in destino:
        destino.append(y)
        cantidad.append(counter)

datos = {
    'Destino': destino,
    'Cantidad': cantidad
}

df = pd.DataFrame(datos)

print(df)


ptl.barh(df['Destino'],df['Cantidad'] , color = ["blue","black","yellow"] )
ptl.title('Destinos turisticos')

ptl.show()
