a = int(input("NUMERO 1:"))
b = int(input("NUMERO 2:"))

def mayor(x,y):
    if x > y:
        return x
    else:
        return y

def menor(x,y):
    if x < y:
        return x
    else:
        return y
found = False
mayor,menor = mayor(a,b) , menor(a,b)
while found==False:
    res = mayor  % menor
    div = mayor  / menor
    
    if  res==0:
        found=True
        print("MCD ",menor)        
    else:
        
        cal = menor * round(div)
        resta = mayor - cal
        mayor,menor = menor , resta
