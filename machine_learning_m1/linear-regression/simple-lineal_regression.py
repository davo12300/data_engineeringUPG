len_data = int(input('INGRESE LA CANTIDAD DE DATOS QUE DESEA:\t'))

x = [int(input(f'Variable independiente {n+1}: \t')) for n in range(len_data) ]
print()
y = [int(input(f'Variable dependiente {n+1}: \t')) for n in range(len_data) ]

## Calculo de producto de x por y x al cuadrado para cada uno de los datos
producto_xy = []
x_cuadrada = []

for i in range(len(x)):
    producto_xy.append((x[i]*y[i]))
    x_cuadrada.append(x[i]**2)

## PENDIENTE B0
B0_pendiente = ((len(x) * sum(producto_xy))-(sum(x) * sum(y))) / ((len(x) * sum(x_cuadrada))-(sum(x)**2))

## INTERSERCCION B1
B1_interseccion = (sum(y)/len(y)) - (B0_pendiente * (sum(x)/len(x)))

x_prediccion = int(input('VALOR DE X PARA PREDICCIÓN:\t'))

y_prediccion = B1_interseccion + B0_pendiente * x_prediccion

print(f"LA PREDICCION DE Y SERÁ: \t {y_prediccion} \n CUANDO LA VARIABLE INDEPENDIENTE ES:\t {x_prediccion}")


