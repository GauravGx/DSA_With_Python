
# Q1 : Define a class Node to descrive a node of singly Linked list


class Node:
    def __init__(self,item = None,next = None):
            self.item = item
            self.next = next


# Q2 : Define a class Sll to implement Singlylink list with __init__() method to create and initialise start reference variable
# Q3 : Define a method to check list is empty or not
# Q4 : Define a method insert_at_start() to insert an element at the starting of the list
class SLL:
    def __init__(self,start = None):  # creating a start pointer
        self.start = start
   
    def is_empty(self):             # for checking node exist or not
          return self.start == None
    
    def insert_at_start(self,data): # insert at first node
          newnode = Node(data,self.start)
          self.start = newnode
                
    def insert_at_last(self,data):
           newnode = Node(data)
           if not self.is_empty():
                 temp = self.start
                 while temp.next is not None:
                       temp = temp.next
                 temp.next = newnode
           else:
                 self.start = newnode           
                
   
    def Search_Node(self,data):
          temp = self.start
          while temp is not None:
                     if temp.item == data:
                          return temp
                     temp = temp.next
          return None        

    def Insert_After(self,data,nodeN):
              temp = self.start
              while nodeN > 1 and temp is not None:
                     temp = temp.next
                     nodeN=nodeN - 1
              newnode = Node(data,temp.next)
              temp.next = newnode 

    def print_List(self):
          temp = self.start
          while temp is not None:
                print(temp.item,end=" ")
                temp = temp.next
          

    def Delete_at_first(self):
            if self.start is not None:
                  self.start = self.start.next

    def Deltete_at_last(self):
           if self.start is None:
                 pass
           elif self.start.next is None:
                 self.start = None
           else:
                 temp = self.start
                 while temp.next.next is not None:
                       temp = temp.next 

                 temp.next = None 


    def delete_item(self,data):
          if self.start is None:
                pass
          elif self.start.next is None:
                if self.start.item == data:
                      self.start = None 

          else:
                temp = self.start
                if temp.item == data:
                      self.start = temp.next
                else:
                      while temp.next is not None:
                            if temp.next.item == data:
                                  temp.next = temp.next.next
                                  break     
                            temp = temp.next
      #     def __iter__(self):
      #         return SLLIterator(self.start)
                               
                    
# def SLLIterator():
#       def __init__(self,start):
#               self.current = start

#       def __iter__(self):
#             return self

#       def __next__(self):
#              if not self.current:
#                    raise StopIteration
#              data = self.current.item
#              self.current = self.current.next
#              return data
            


     

# #driver Code
# mylist = SLL()
# mylist.insert_at_start(10)
# mylist.insert_at_start(20)
# mylist.insert_at_start(30)
# mylist.insert_at_start(40)
# mylist.print_List() 
# mylist.delete_item(20)
# print()
# mylist.print_List()








