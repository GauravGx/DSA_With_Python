#circular Doubly Link List code


class Node:
    def __init__(self,item=None,prev=None,next=None):
            self.prev=prev
            self.item=item
            self.next=next




class CDLL:
      def __init__(self,start=None):
             self.start = start

      def is_Empty(self):
            return self.start is None


      def insert_at_start(self,data):
            newnode = Node(data)
            if self.is_Empty():
                  newnode.next = newnode
                  newnode.prev = newnode
                  self.start = newnode
            else:
               newnode.next = self.start
               newnode.prev = self.start.prev
               self.start.prev.next = newnode
               self.start.prev = newnode

            self.start = newnode


      def insert_at_last(self,data):
            newnode = Node(data)
            if self.is_Empty():
                  newnode.next = newnode
                  newnode.prev = newnode
                  self.start = newnode
            else:
                  newnode.next = self.start
                  newnode.prev = self.start.prev
                  self.start.prev.next = newnode
                  self.start.prev = newnode           

     
      def search(self,data):
            temp = self.start
            if temp == None:
                  return None
            else:
                  temp = self.start
                  while True:
                        if temp.item == data:
                              return temp
                        temp = temp.next
                        if temp == self.start:
                              break
                  return None      
            
      def insert_after(self,temp,data):
            if temp is not None:
                  newnode = Node(data)
                  newnode.next = temp.next
                  newnode.prev = temp
                  temp.next.prev = newnode
                  temp.next = newnode

      def print(self):
            temp = self.start
            if temp == None:
                  return None
            else:
                  temp = self.start
                  while True:
                        print(temp.item,end=' ')
                        temp = temp.next
                        if temp == self.start:
                              break
                  return None  


      def delete_first(self):
            if self.start is not None:
                  if self.start.next == self.start:
                          self.start = None
                  else:
                        self.start.prev.next = self.start.next
                        self.start.next.prev = self.start.prev
                        self.start = self.start.next       


      def delete_last(self):
             if self.start is not None:
                  if self.start.next == self.start:
                          self.start = None
                  else:
                         self.start.prev.prev.next = self.start
                         self.start.prev = self.start.prev.prev
               
                    
      def delete_item(self,data):
            if self.start is not None:
                  temp = self.start
                  if temp.item ==data:
                     self.delete_first()
                  else:
                        temp = temp.next
                        while temp is not self.start:
                              if temp.item == data:
                                    temp.next.prev = temp.prev
                                    temp.prev.next = temp.next   



cll = CDLL()
cll.insert_at_start(10)
cll.insert_at_start(20)
cll.insert_at_last(30)
cll.insert_at_last(40)
cll.print()
