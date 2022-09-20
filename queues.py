queue=[]
def enqueue ():
    element = input("enter your element:")
    queue.append(element)
    print (element, "addeed")
def dequeue():
    if len(queue) == 0:
        print ("queue is empty")
    else:
        deq =queue.pop(0)
        print (deq, "removed")
def display():
    print(queue)

print(enqueue())
dequeue()                                                                              
display()

