# IMPORT OF RANDOM LIBRARY  FOR GENERATE RANDOM NUMBERS

import random

## WELCOME TO THE GAME 
print("-----------------------------------------------")
print("--------------BIENVENIDO AL JUEGO--------------")
print("-----------------------------------------------")

## VARIABLE TO SCORE OF GAME, STARTS IN 0 AND INCREMENT DEPENDS OF GAME
suma = 0 

while suma<=80:
    ## INPUT TO USER PLAY THE GAME
    x = int(input("PRESIONA 1 PARA TIRAR EL DADO\t"))
    if x==1:
        # USE OF RANDOM FUNTION IN RANGE 1 TO 7 LIKE A REAL DICE
        dado = random.randrange(1,7)
        # THE NUMBER OF DICE IS ADDED TO SCORE
        print("HA CAIDO",dado)
        suma = suma + dado
        
    else:
        ## VALIDATION INPUT 
        print("OPCION ERRONEA")
    ## PRINT SCORE 
    print("TU PUNTAJE ES \t", suma)

    ## IF SCORE GETS 30,15, 60 OR 70 THE SCORE SUBSTRACT 3 POINTS
    if suma==30 or suma ==15 or suma==20 or suma==60 or suma==70:
        print("COMO TU SUMA ES ",suma, "RESTAREMOS 3 ")
        suma = suma -3
        print("TU NUEVO PUNTAJE ES",suma)

## THE GAME FINISH  WHEN SCORE IS MAYOR OR EQUALS TO 80
print("-----------------------------------------------")
print("-----------------FIN DEL JUEGO----------------")
print("-----------------------------------------------")
