class Node:
    def __init__(self,data=None,next =None):
        self.data = data
        self.next = next



class Stack:

    def __init__(self):
        self.TOP = None
        self.Countdata = 0

    def is_empty(self):
        return self.TOP is None  

    def push(self,data):
        newnode = Node(data,self.TOP)
        self.TOP = newnode
        self.Countdata += 1

    def pop(self):
       if not self.is_empty(): 
        data = self.TOP.data
        self.TOP = self.TOP.next
        self.Countdata -= 1 
        return data 
       else:
           raise IndexError("Stack is Empty") 


    def peek(self):
        if not self.is_empty():
           return self.TOP.data
        else:
            raise IndexError("stack is Empty")  

    def Size(self):
        return self.Countdata
                   



s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("total element ",s1.Size())
print("TOP element ",s1.peek())
print("Pop Elements ",s1.pop())
print("total element ",s1.Size())


