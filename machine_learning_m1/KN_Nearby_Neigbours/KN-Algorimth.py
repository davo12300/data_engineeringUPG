import openpyxl
import pandas as pd 

##acceso al documento
doc= openpyxl.load_workbook("clasicos.xlsx")
##acceso a la hoja
hoja = doc.get_sheet_by_name("Hoja1")
kilometraje,precio = [],[]

##EXTRACCIÓN DE DATOS 

for row in hoja.iter_rows():
    a = row[0].value
    b = row[1].value
    kilometraje.append(a)
    precio.append(b)

## ELIMINAR TITULO DE COLUMNA / DROP COLUMN TITTLE
kilometraje.remove(kilometraje[0])
precio.remove(precio[0])

## INGRESO DE VECINOS CERCANOS
k = int(input("INGRESA LA CANTIDAD DE MENORES: \t "))

# ESTA FUNCION VERIFICA CUALES SON LOS NUMEROS CERCANOS AL KILOMETRAJE A EVALUAR 
def verificar(valor, arreglo):
    frame = []
    for x in range(len(arreglo)):
        op = valor - arreglo[x]
        if op > 0:
            frame.append(op)
        else:
            frame.append(op*-1)
    indice = 0
    for c in range(len(frame)):   
        if frame[c] == min(frame):
            indice = c
            
            break    
    return(indice)

## SI SON MAS DE 6 VECINOS SERA INVALIDO
if k > 6:
    print('ERROR, K-NEIGHBOUR INVALIDO')

else:
    ## INGRESO DEL KILOMETRAJE A EVALUAR 
    valor_kilometraje = int(input("\nINGRESE EL KILOMETRAJE A VALUAR: \t "))
    data = []
    precios_encontrados , kilometrajes_encontrados= [], []
    ## SEGUN LOS VECINOS A EVALUAR SE EJECUTAR LA FUNCION QUE ENCUENTRA CUALES SON LOS VECINOS CERCANOS 
    for n in range(k):
        
        kilometrajes_encontrados.append(kilometraje[verificar(valor_kilometraje,kilometraje)])
        precios_encontrados.append(precio[verificar(valor_kilometraje,kilometraje)])
        kilometraje.remove(kilometraje[verificar(valor_kilometraje,kilometraje)])
				precio.remove(precio[verificar(valor_kilometraje,kilometraje)])
    
    datos = {
        'Kilometraje Relacionado': kilometrajes_encontrados,
        'Precios Relacionados': precios_encontrados
    }
    ## IMPRESION DE VALORES
    df = pd.DataFrame(datos)

    print('\n',df,'\n')

    valor_final = round((sum(precios_encontrados)/ len(precios_encontrados)),2)
    print('PARA UN AUTOMOVIL CON',"{:,}".format(valor_kilometraje),'KM RECORRIDOS\nSE TENDRÁ UN',
          
          'VALOR CALCULADO DE : \t $',"{:,}".format(valor_final)
          
          
          )
