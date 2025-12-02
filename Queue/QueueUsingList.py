 
class Queue:

    def __init__(self):
        self.front = []
        self.rear = None

    def is_empty(self):
        return len(self.front) == 0 

    def enqueue(self,data):
           self.front.append(data)
           self.rear = data

    def dequeue(self):
        if not self.is_empty():
            self.rear = self.front.pop(0)
            

    def get_front(self):
        if not self.is_empty():
            return self.front[0]
    

    def get_rear(self):
        if not self.is_empty():
         return self.rear
    
    def Size(self):
        return len(self.front)
    

q1 = Queue()
q1.enqueue(10)    
q1.enqueue(20)    
q1.enqueue(30)    
print("last data is ",q1.get_rear())  
print("first data is ",q1.get_front())  
print("Size of Queue is ",q1.Size())  

q1.dequeue()

print("last data is ",q1.get_rear())  
print("first data is ",q1.get_front())  
print("Size of Queue is ",q1.Size())  





        