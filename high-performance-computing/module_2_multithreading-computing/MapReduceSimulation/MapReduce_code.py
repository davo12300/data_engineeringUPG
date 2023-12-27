import openpyxl
import threading,time

##ACCESO AL DOCUMENTO
doc= openpyxl.load_workbook("Agua_Calidad.xlsx")
##ACCESO A LA HOJA
hoja = doc.get_sheet_by_name("Agua_Calidad")


###FUNCION DE CALCULO
def op(state,tipo):
    ##Recibe y normaliza a mayusculas la entrada de texto
    state=state.upper()
    ## counter para sumar el tipo de calculo que es y conter_t el total de posiciones sumadas
    counter,t_counter= 0,0
    ## column sirve para seleccionar la columna de impresion según en tipo de calculo requerido
    colum=['','Poblacion Total','Eficiencia Cloracion','Dentro de la norma']
    
    ## Iteración de hojas, segun el estado y el tipo de calcula, counter y counter_t haran sus respectivos incrementos
    for row in hoja.iter_rows():
        ## estado ingresado se encuentra en la columna 0 
        # entonces sumara las mismas posiciones pero en la columna del tipo de calculorequerido
        if row[0].value ==state:
            counter = counter + row[tipo].value
            t_counter=t_counter+1 
    ## define si el total sumado sera un total o un promedio        
    if tipo!=1:
        counter=round(counter/t_counter,2)
    ## impresion de resultados
    print('PARA', state,' ',colum[tipo],':\t',counter)


##Agrega los valores de municipio y tipo de calculo
municipio = []
tipode = []

##Captura de solicitudes
for x in range(5):
    municipio.append(str(input("INGRESA EL ESTADO:\t")))
    print('1 POBLACION TOTAL |2 EFICIENCIA DE CLORACION |3 DENTRO NORMA|')
    tipode.append(int(input("OPCION:\t")))

t1= threading.Thread(target=op, args=(municipio[0],tipode[0]))
t2= threading.Thread(target=op, args=(municipio[1],tipode[1]))
t3= threading.Thread(target=op, args=(municipio[2],tipode[2]))
t4= threading.Thread(target=op, args=(municipio[3],tipode[3]))
t5= threading.Thread(target=op, args=(municipio[4],tipode[4]))

## INICIALIZA HILOS

t1.start()
time.sleep(1)
t2.start()
time.sleep(1)
t3.start()
time.sleep(1)
t4.start()
time.sleep(1)
t5.start()
