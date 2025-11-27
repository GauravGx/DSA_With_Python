# append()
# clear()
# copy()
# count()
# extend()
# index()
# insert()
# pop()
# remove()
# reverse()
# sort()

# these are list class methods

class Stack(list):        # extended list class

    def __init__(self):
        self.stack = []
        
    def is_empty(self):
        return len(self.stack) == 0

    def push(self,data):
         self.stack.append(data)
        
    def pop(self):
       if not self.is_empty(): 
          return self.stack.pop()
       else:
           raise IndexError("Stack is Empty")

    def peek(self):
        if not self.is_empty():
         return self.stack[len(self.stack) - 1 ]
        else:
            raise IndexError("Stack is empty")
        
    
    def size(self):
        return len(self.stack)   
    


s1 = Stack() 

s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.push(50)

print(s1.is_empty())
print(s1.pop()) 
print(s1.peek())
print(s1.size())
print(s1.peek())
             
