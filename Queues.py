import queue


#FIFO first in first out example of python queues
q = queue.Queue()
numbers = [10,20,30,40,50,60,70,80,90]
for number in numbers:
    q.put(number)
print('fifo\n')
print(q.get())
print(q.get())

#LIfo example
q1 = queue.LifoQueue()
for number in numbers:
    q1.put(number)

print('lifo\n')
print(q.get())
print(q.get())

#priority queue

q3=queue.PriorityQueue()
q3.put((3,"hello world"))
q3.put((11,'hello world'))
q3.put((5,'hello world'))
q3.put((1,True))

while not q3.empty():
    print(q3.get())
    