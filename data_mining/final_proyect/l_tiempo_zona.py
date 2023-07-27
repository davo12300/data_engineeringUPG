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

years_selected = []
for f in years:
    if (f not in years_selected) ==True:
        years_selected.append(f)



data_municipios = ['Cortazar','Celaya','Villagrán','Salamanca']

count_year = []
accidentes = []


for x in range(len(years_selected)):

    contador = 0
    for y in range(len(data_municipios)):

        for z in range(len(municipio)):

            
            if  int(years_selected[x])==years[z] and data_municipios[y]==municipio[z] and tipo[z]==1006000039:
                
                
                contador=contador+cantidad[z]

    
    count_year.append(contador)




info = {

    'YEAR': years_selected,
    'Cantidad de Accidentes':count_year

}
df = pd.DataFrame(info)

print(df)


umbral = 5
# Crear una lista para almacenar los colores de las barras
fig, ax = ptl.subplots()
ax.plot(df['YEAR'],df['Cantidad de Accidentes'],color="red")
# Etiquetas y título
ptl.xlabel('Linea Temporal')
ptl.ylabel('Cantidad de accidentes')
ptl.title('Víctimas de accidentes Celaya, Cortazar y Villagrán')
ptl.xticks(rotation=45,ha='right')
ptl.tight_layout()
# Mostrar la gráfica
ptl.show()

