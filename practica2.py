import random

##SE CREA EL ARREGLO VACIO

arreglo = []

##CADA REPETICION AÑADIRA UN VALOR ENTRE 1 Y 0 DE MANERA RANDOM
##NOTA: SE PUEDE CAMBIAR A AÑADIR MANUALMENTE  CADA VALOR
# CON INT(INPUT) , SE HACE RANDOM PARA MAS PRACTICO
for x in range(0,5):
    arreglo.append(random.randrange(0,2))

#IMPRIMIMOS EL ARREGLO
print(arreglo)

#COMENZAMOS COEFICIENTE EN 16 PUES ESTE ES COMO SI FUERA EL 2 CON EXPONENTE 4 QUE 
# USAMOS AL CONVERTIR A BINARIO 
coef=16
#TOTAL SERA NUESTRO NUMERO BINARIO CONVERTIDO A DECIMAL
total = 0

##RECORREMOS EL ARREGLO NUEVAMENTE , 0 A 5 PUES ES DE IZQUIEDA A DERECHA
for x in range(0,5):
    ##CADA REPETICION VALUAREMOS LA POSICION, SI ESTA TIENE UN "1" SUMAREMOS EL COHEFICIENTE
    # A NUESTRO TOTAL 
    if arreglo[x]==1:
        total=total+coef
    #CON FORME VAMOS RECORRIENDO AL ARREGLO TENEMOS QUE REDUCIENDO EL COHEFICIENTE , POR ELLO
    # LO DIVIDIREMOS ENTRE DOS PARA QUE CADA REPETICION VAYA DE 16 A 8, DE 8 A 4 Y DE 4 A 2 ETC.    
    coef=coef/2

##AL FINAL IMPRIMIMOS EL ARREGLO
print("su numero en binario es:  ",total)
