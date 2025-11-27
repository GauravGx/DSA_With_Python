
# crating a stack inheriting list class


class stack(list):

    def is_empty(self):
        return len(self) == 0
    

    def push(self,data):
        self.append(data)

    def pop(self):               # override parent class pop method
        if not self.is_empty():      
          return super().pop()         # call parent class pop method    
        else:
           raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self[-1]   # last element of stack
        else:
            raise IndexError("stack is empty")
        
    def size(self):
        return len(self)   
    
    def insert(self,index,data):
        raise AttributeError("No attribure 'insert' in stack ")
    


s1 = stack()
s1.push(10)
s1.push(10)
s1.push(20)
s1.push(30)
print("top value ",s1.peek() )


print(s1.pop())
print("top value ",s1.peek() )

