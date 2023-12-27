x = int(input("INGRESA EL NUMERO: "))

def verify(numero):
    if numero == 0 or numero == 1:
        return False
    for i in range (2, int (numero/2)):
        if numero % i == 0: 
            return False
    return True

def factores(x):
    primos,divi = [], []
    if x == 4:
        return [2,2]
    if verify(x) == True:
        return [x]
    else:
        for y in range(x):
            if verify(y) == True:

                primos.append(y)
        c, t , secuencia= x, 0,[]
        while c >= 1:
            
            if c % primos[t]==0:

                secuencia.append(primos[t])
                
                divi.append(int(c))
                c = c / primos[t] 
            else:        
                if c<=1: 
                    break
                t = t +1
    return secuencia

n=1
fact = factores(x)
print(1, ',', x)
for z in range(2,x):
    
    cont = 0
    fact_y = factores(z)
    
    for y in fact_y:
        
        if y not in fact:
            cont = cont + 0
        else:
            cont = cont + 1
    if cont>0:
        
        n = n + 0
        
    else:
        n = n +1
        print(z, ',', x)
        
        
        
print('# PRIMOS RELATIVOS',n)
