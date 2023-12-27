x = int(input("INGRESA EL NUMERO: "))

def verify(num):
    e = 0
    for i in range(1 , num+1):
        if num % i ==0:
            e=e+1        
    if e > 2:             
        return True
    else:
        if e == 2:
            return False

primos,divi = [], []
if verify(x) == False:
    print('ES NUMERO PRIMO')
else:
    for y in range(x):
        if verify(y) == False:
           primos.append(y)
    c, t , secuencia= x, 0,[]
    while c >= 1:
        
        if c % primos[t]==0:
            secuencia.append(primos[t])
            
            divi.append(c)
            c = c / primos[t] 
        else:        
            if c<=1: 
                break
            t = t +1



for z in range(len(secuencia)):
    print( divi[z], '|', secuencia[z])
