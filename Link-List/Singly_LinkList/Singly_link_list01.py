
class Node:
    def __init__(self,data):
        self.data = data
        self.Next = None


class SSL():
    def __init__(self):
          self.Head = None

    def InsertNode(self,data):
          NewNode = Node(data)
          if not self.Head:
               self.Head = NewNode
               return 
          else:
               current = self.Head
               while(current.Next != None):
                         current = current.Next 
            
               current.Next = NewNode
    
    def showNode(self):
           current =  self.Head 
           while(current):
                 print(f" DATA : {current.data}")
                 current = current.Next  


l1 = SSL()   
l1.InsertNode(10)
l1.InsertNode(20)
l1.InsertNode(30)

l1.showNode()
                              

       
          




