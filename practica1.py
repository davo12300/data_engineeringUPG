import random

## SE CREA EL ARREGLO VACIO
arreglo = []
## CICLO FOR RECORRE DEL 0 AL 10 
for x in range (0,10):
    arreglo.append(random.randrange(15,51))
print(arreglo)

for x in range(0,10):

    if arreglo[x]%3==0:
        arreglo[x]=0
print(arreglo)


