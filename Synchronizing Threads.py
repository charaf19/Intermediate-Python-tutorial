#manage many threads accessing the same source of data 
#the concept of locking 


import threading
import time
x = 8192

lock=treading.Lock()
def double():
    #define a global varial that's accessible in all arround the code 
    global x,lock
    lock.acquire()
    while x <16384
        x*=2
        print(x)
        #sleep method it(s just to track what happend in the code)
        tiem.sleep(1)
    lock.release()
    print('reached the maximum')

def halve():
    global x,lock
    lock.acquire()
    while x>1:
        x/=2
        print(x)
        time.sleep(1)
    lock.release()
    print('reched the minimum')

t1 = treading.Thread(targer=double)
t2= treading.Thread(target=halve)

t1.start()
t2.start()