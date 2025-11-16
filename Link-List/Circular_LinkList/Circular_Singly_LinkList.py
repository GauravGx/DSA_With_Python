class Node:
   def __init__(self,data = None,Next = None):
           self.data = data
           self.Next = Next



class CSLL:
      def __init__(self,last=None):
            self.last = last

      def is_empty(self):
            return  self.last is None

      def  insert_at_start(self,data):
              newnode = Node(data)
              if self.is_empty():
                    newnode.Next = newnode
                    self.last = newnode
              else:
                    newnode.Next = self.last.Next
                    self.last.Next = newnode

      def insert_at_last(self,data):
             newnode =Node(data)             
             if self.is_empty():
                   newnode.Next = newnode
                   self.last = newnode
             else:
                   newnode.Next = self.last.Next
                   self.last = newnode   


      def search_list(self,data):
            if not self.is_empty():
                  temp = self.last.Next
                  while temp.Next != self.last.Next:
                         if temp.data == data:
                               return temp
                         temp = temp.Next
                         
            if temp.data == data:
                 return temp    
            return None       
                  

      def insert_after(self,temp,data):
             if temp is not None:
                   newnode = Node(data,temp.Next)
                   temp.Next = newnode
                   if temp == self.last:
                         self.last = newnode

      def print_list(self):                      
             if not self.is_empty():
                   temp = self.last.Next
                   while temp != self.last:
                         print(temp.data,end='')
                         temp = temp.Next
                   print(temp.data) 


      def delete_first(self):
           if not self.is_empty():
                 if self.last.Next == self.last:
                       self.last = None
                 else:
                       self.last.Next = self.last.Next.Next      


     
      def delete_last(self):
        if not self.is_emplty():
              if self.last.Next == self.last:
                    self.last = None
              else:
                    temp = self.last.Next
                    while temp.Next!= self.last:
                          temp = temp.Next 
                    temp.next = self.last.Next
                    self.last = temp          


      def delete_item(self,data):
           if not self.is_empty():
                 if self.last.Next == self.last:
                       if self.last.data == data:
                             self.last = None
                 else:
                       if self.last.next.data== data:
                             self.delete_first()
                       else:
                             temp = self.last.Next

                             while temp != self.last:
                                  if temp.Next == self.last:
                                        self.delete_last()
                                        break
                                  if temp.Next.data ==data:
                                        temp.Next=temp.Next.Next
                                        break
                                  temp = temp.Next
                              

                  
cll = CSLL()                                        
cll.insert_at_start(10)                       
cll.insert_at_last(20)
cll.insert_at_last(30)
cll.insert_at_last(40)
cll.print_list()

                    
     


