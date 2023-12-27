import threading,time

def op(x,y,s):
    
    if s == 's':
        operacion = x + y
        print('la suma es ', operacion)
    elif s == 'r':
        operacion = x - y
        print('la resta es ', operacion)
    elif s == 'm':
        operacion = x * y
        print('la multiplicacion es ', operacion)
    else:
        if s == 'd':
            operacion = x / y
            print('la division es ', operacion)

t1= threading.Thread(target=op, args=(2,3,'s'))
t2= threading.Thread(target=op, args=(5,3,'r'))
t3= threading.Thread(target=op, args=(4,4,'m'))
t4= threading.Thread(target=op, args=(4,3,'d'))



t1.start()
time.sleep(1)
t2.start()
time.sleep(1)
t3.start()
time.sleep(1)
t4.start()
