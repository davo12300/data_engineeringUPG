## VARIABLES

arreglo = []
contador = 0

## WHILE LOOP WITH COUNTER FOR CAN FINISH HIM
while contador <=20:
    numero = int(input("INGRESAR UN VALOR"))
    ## VALIDATION OF NUMBER MAYOR THAN 20 AND MINOR THAN 50 
    if numero >=20 and numero <=50:
        ## USE OF APPEND FUNCTION 
        arreglo.append(contador)
        arreglo[contador]=numero
        contador=contador +1
    else:
        print("numero no valido")

print(arreglo)
