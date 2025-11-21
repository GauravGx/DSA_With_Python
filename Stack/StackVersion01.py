class Stack:
    def __init__(self):
        self.peek = -1
        self.S1 = []

    def push(self, data):
        self.S1.append(data)
        self.peek += 1

    def pop(self):
        if self.peek == -1:
            print("Stack is Empty")
            return None
        self.peek -= 1
        return self.S1.pop()

    def top(self):
        if self.peek == -1:
            print("Stack is Empty")
            return None
        return self.S1[self.peek]

    def print_data(self):
        for x in self.S1:
            print(x)

    def size(self):
        return self.peek + 1
           
                

st = Stack()
st.print_data()
print(st.top())
st.push(10)
st.push(20)
st.push(30)
st.print_data()
print(st.top())
st.pop()
st.print_data()
print(st.size())


