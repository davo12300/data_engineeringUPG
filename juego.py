import random


print("-----------------------------------------------")
print("--------------BIENVENIDO AL JUEGO--------------")
print("-----------------------------------------------")

suma = 0 
while suma<=80:
    x = int(input("PRESIONA 1 PARA TIRAR EL DADO"))
    if x==1:
        dado = random.randrange(1,6)
        print("HA CAIDO",dado)
        suma = suma + dado
        
    else:
        print("OPCION ERRONEA")
    
    print("TU PUNTAJE ES ", suma)
    
    if suma==30 or suma ==15 or suma==20 or suma==60 or suma==60:
        print("COMO TU SUMA ES ",suma, "RESTAREMOS 3 ")
        suma = suma -3
        print("TU NUEVO PUNTAJE ES",suma)
print("FIN DEL JUEGO")
