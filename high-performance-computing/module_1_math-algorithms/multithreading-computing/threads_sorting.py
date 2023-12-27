import threading,time
def op(datos,s):
    
    if s == 's':    
        print('ASCENDENTE:\t',sorted(datos), '\n')
    else:
        print('DESCENDENTE:\t',sorted(datos, reverse=True))
    
array = []

for n in range(10):
    array.append(int(input('INGRESA UN DATO: \t')))
    t1= threading.Thread(target=op, args=(array,'s'))
    t1.start()
    time.sleep(1)
    t2= threading.Thread(target=op, args=(array,'r'))
    t2.start()
