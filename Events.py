import threading 
event = threading.Event()
def myfunction():
    print("waiting for event to trgger\n")
    event.wait()
    print('performing the action xyz now\n')

t1 = treading.Thread(target=myfunction)
t1.start()
x = input("do you want to trigger the event(y/n)\n")
if x=='y':
    event.set()
