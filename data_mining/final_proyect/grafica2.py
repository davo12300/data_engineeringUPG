import openpyxl
import pandas as pd 
import matplotlib.pyplot as ptl

##acceso al documento
doc= openpyxl.load_workbook("guanajuato.xlsx")
##acceso a la hoja
hoja = doc.get_sheet_by_name("Hoja1")
years, tipo, cantidad,municipio = [],[],[],[]

##EXTRACCIÓN DE DATOS 

## años
for row in hoja.iter_rows():
    a = row[6].value
    b = row[4].value
    c = row[7].value
    d = row[3].value
    years.append(a)
    tipo.append(b)
    cantidad.append(c)
    municipio.append(d)

#ELIMINAR PRIMERA FILA

years.remove(years[0])
tipo.remove(tipo[0])
cantidad.remove(cantidad[0])
municipio.remove(municipio[0])
##definicion de cuentas


#Sacar cantidad de municipios

data_municipios = []
for z in municipio:
    if (z not in data_municipios) ==True:
        data_municipios.append(z)

data_municipios.remove(data_municipios[0])

accidentes = []

for x in range(len(data_municipios)):
    contador = 0
    for y in range(len(municipio)):

        if municipio[y] ==data_municipios[x] and tipo[y]==6200009438 and years[y]==2019:
            contador= contador + cantidad[y]

    
    accidentes.append(contador)

        
info = {

    'Municipios': data_municipios,
    'Cantidad de Accidentes':accidentes

}
df = pd.DataFrame(info)

umbral = 5
# Crear una lista para almacenar los colores de las barras
colores = ['#008000' if cantidad < umbral else '#8B0000' for cantidad in df['Cantidad de Accidentes']]
# Crear la gráfica de barras horizontales con los colores personalizados
ptl.barh(df['Municipios'], df['Cantidad de Accidentes'], color=colores)
# Etiquetas y título
ptl.xlabel('Cantidad de Accidentes')
ptl.ylabel('Municipios')
ptl.title('Víctimas de accidentes 2019')
# Mostrar la gráfica
ptl.show()

