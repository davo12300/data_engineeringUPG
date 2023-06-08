import math
import openpyxl

##acceso al documento
doc= openpyxl.load_workbook("pesos.xlsx")
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

intervalos  = round(1 + (3.322 * (math.log(len(datos_lista),10))))  
amplitud = rango/intervalos


##LISTAS QUE CONTENDRAN LOS LIMITES Y LA FRECUENCIA DE LOS DATOS
l_inferior = []
l_superior = []
frec_data = []

calculo= min(datos_lista)
for x in range(intervalos):

    
    l_inferior.append(calculo)
    l_superior.append(calculo+amplitud)
    calculo = calculo + amplitud
    counter= 0
    for i in range(len(datos_lista)):
        
        if datos_lista[i] >= l_inferior[x] and datos_lista[i] <= l_superior[x]:
            
            counter = counter + 1 
        
    frec_data.append(counter)
    
    counter= 0

fi_data = []
suma, media= 0 , 0
for i in range(len(frec_data)):
    suma = suma + frec_data[i]
    
    fi_data.append(suma)

m_clase = []
for t in range(len(l_superior)):
    sumatoria= round(((l_inferior[t] + l_superior[t] )/ 2),2)
    m_clase.append(sumatoria)

frec_relativa = []
for a in range(len(frec_data)):
    result = round(frec_data[a] / len(datos_lista),2)
    frec_relativa.append(result)

fi_xi = []
suma_fi = 0
for r in range(len(m_clase)):
    operation= round((frec_data[r] * m_clase[r]),2)
    fi_xi.append(operation)
    suma_fi = suma_fi + operation

##MEDIANA

dato = len(datos_lista)/2

frame = []
for x in range(len(fi_data)):
    op = dato - fi_data[x]
    if op > 0:
        frame.append(op)
    else:
        frame.append(op*-1)
print(min(frame))
indice = 0
for c in range(len(frame)):   
    if frame[c] == min(frame):
        indice = c
        break

calculo_mediana = l_inferior[indice] + ( ((len(datos_lista)/2) - (fi_data[indice-1]))/ frec_data[indice] ) * (l_inferior[indice]-l_superior[indice])


#MODA

position = 0 
convert = frec_data
for c in range(len(convert)):   
    if convert[c] == max(convert):
        position = c
        break
if position == 0:
    bug = convert[0]
    convert[0] = 0
    print(max(convert))
    position = max(convert)
    for d in range(len(frec_data)):
        if convert[d] == max(convert):
            position = d
            convert[0] = bug 
            break
p = position
operacion_moda = (l_inferior[p]) + (( frec_data[p] - frec_data[p-1] )/(  ( frec_data[p] - frec_data[p-1] ) + (frec_data[p] - frec_data[p+1] ) ))




##IMPRESION DE RESULTADOS

print('INTERVALOS \t| fi\t| FI\t| xi\t| fr\t| fi*xi\t')
for q in range(len(frec_data)):
    print(round(l_inferior[q],2) ,'-', round(l_superior[q] ,2),'\t|' ,frec_data[q],'\t|',fi_data[q], '\t|', m_clase[q],'\t|',frec_relativa[q],'\t|',fi_xi[q])

print('S:\t' , round(suma_fi,3))
print('MEDIA:\t', round( (suma_fi/len(datos_lista)),3))
print('MEDINA:\t', round(calculo_mediana,2))
print('MODA:\t', round(operacion_moda,2))


    
