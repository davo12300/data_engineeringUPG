import math
datos_lista = [10,12,10,11,17,15,22,25,14,19]
rango = max(datos_lista) - min(datos_lista)

intervalos  = round(1 + (3.322 * (math.log(len(datos_lista),10))))  
amplitud = rango/intervalos
print(intervalos, amplitud)

l_inferior = []
l_superior = []
frec_data = []

calculo= min(datos_lista)
for x in range(intervalos):

    print(x)
    l_inferior.append(calculo)
    l_superior.append(calculo+amplitud)
    calculo = calculo + amplitud
    counter= 0
    for i in range(len(datos_lista)):
        
        if datos_lista[i] >= l_inferior[x] and datos_lista[i] <= l_superior[x]:
            
            counter = counter + 1 
        
    frec_data.append(counter)
    
    counter= 0


print(frec_data)

fi_data = []
suma= 0
for i in range(len(frec_data)):
    suma = suma + frec_data[i]
    fi_data.append(suma)

print(fi_data)

m_clase = []
for t in range(len(l_superior)):
    sumatoria= (l_inferior[t] + l_superior[t] )/ 2
    m_clase.append(sumatoria)

print(m_clase)

frec_relativa = []
for a in range(len(frec_data)):
    result = frec_data[a] / len(datos_lista)
    frec_relativa.append(result)
print(frec_relativa)


    
