from list import *

class Stack:
    def __init__(self):
        self.mylist = SLL()
        self.countdata = 0

    def is_empty(self):
        return self.mylist.is_empty()
    
    def push(self,data):
        self.mylist.insert_at_start(data)
        self.countdata += 1

    def pop(self):
        if not self.is_empty():
            self.mylist.Delete_at_first()
            self.countdata -= 1

    def peek(self):
        if not self.is_empty():
            return self.mylist.start.item


    def Size(self):
        return self.countdata   


s1 = Stack()             
s1.push(10)        
s1.push(20)        
s1.push(30)        
s1.push(40)
print(s1.Size())

print("Top of Value is ",s1.peek())


