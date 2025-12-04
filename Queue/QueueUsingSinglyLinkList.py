class Node:
    def __init__(self,item = None,next = None):
          self.item = item
          self.next = next


class Queue:
     
     def __init__(self):
          self.front = None
          self.rear = None
          self.countdata = 0


     def is_empty(self):
              return self.front == None


     def enqueue(self,data):
           newnode = Node(data)
           if self.is_empty():
                 self.front = newnode
           else:
                  self.rear.next = newnode

           self.rear = newnode
           self.countdata += 1 

     def dequeue(self):
           if self.is_empty():
                 raise IndexError("empty Queue")
           elif self.front == self.rear:
                 self.front = None
                 self.rear = None
           else:
                 self.front = self.front.next 
                           

           self.countdata -= 1     
              

     def get_front(self):
           if self.is_empty():
                 raise IndexError("No data in the queue")
           else:
                 return self.front.item

     def get_rear(self):
           if self.is_empty():
                 raise IndexError("No data in the queue")
           else:
                return self.rear.item 


     def Size(self):
           return self.countdata     





q1 =  Queue()

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
print("size is ",q1.Size())
print("front data is ",q1.get_front())
print("Rear data is ",q1.get_rear())

q1.dequeue()

print("size is ",q1.Size())
print("front data is ",q1.get_front())
print("Rear data is ",q1.get_rear())



                                
 

