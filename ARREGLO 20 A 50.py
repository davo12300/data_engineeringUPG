arreglo = []
contador = 0


while contador <=20:
    numero = int(input("INGRESAR UN VALOR"))
    
    if numero >=20 and numero <=50:
        arreglo.append(contador)
        arreglo[contador]=numero
        contador=contador +1
    else:
        print("numero no valido")

print(arreglo)
