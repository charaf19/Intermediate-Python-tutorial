import threading
def HelloWorld():
    print('hello world')

#we don't run the fonction we just call it 
#the thread are just used to speed up our script and make functions work in parallel
t1= threading.Thread(target=HelloWorld)
#start the thread 
t1.start()
def function1():
    for x in range(10000):
        print("OK1")
def function2():
    for x in range(4000):
        print("OK2")

t1 = threading.Thread(target=function1)
t2= threading.Thread(target=function2)

t1.start()
t2.start()

#to not execute another code until i finish the thread 
def helllo():
    for x in range(50):
        print(hello)

t=threading.Thread(target=hello)
t.start()
t.join()
print('the thread is finished ')