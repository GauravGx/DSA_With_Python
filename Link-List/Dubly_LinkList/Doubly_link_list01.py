'''Doubly Link List with all operation'''

class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.next = next
        self.item = item


class DLL:

    def __init__(self, start=None):
        self.start = start

    def isEmpty(self):
        return self.start is None

    def insert_at_start(self, item):
        newnode = Node(None, item, next=self.start)
        if not self.isEmpty():
            self.start.prev = newnode
        self.start = newnode

    def insert_at_last(self, item):
        newnode = Node(item=item)
        if self.isEmpty():
            self.start = newnode
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = newnode
            newnode.prev = temp

    def insert_at_last2(self, item):
        temp = self.start
        if self.start != None:
            while temp.next != None:
                temp = temp.next

        newnode = Node(temp, item, None)
        if temp == None:
            self.start = newnode
        else:
            temp.next = newnode

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            else:
                temp = temp.next
        return None

    def insert_after(self, temp, data):
        if temp is not None:
            newnode = Node(temp, data, temp.next)
            if temp.next is not None:
                temp.next.prev = newnode
            temp.next = newnode

    def print_list(self):
        if self.start is not None:
            temp = self.start
            while temp is not None:
                print(temp.item)
                temp = temp.next

    def delete_at_first(self):
        if self.start is not None:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None

    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None

    def delete_item(self, data):
        if self.start is None:
            pass
        else:
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    if temp.next is not None:
                        temp.next.prev = temp.prev
                    if temp.prev is not None:
                        temp.prev.next = temp.next
                    else:
                        self.start = temp.next
                    break
                temp = temp.next



mylist = DLL()
mylist.insert_at_start(10)
mylist.insert_at_last(20)
mylist.print_list()
