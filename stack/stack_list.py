class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class stack:
    def __init__(self):
        self.top=None
    def push(self,item):
        new_node=node(item)
        new_node.next=self.top
        self.top=new_node
        print("Deleted elements=",item)
    def pop(self):
        if self.top is None:
                    print("Stack is empty")
        else:
                    print("Top element:",self.top.data)
                    self.top=self.top.next
    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Top element:",self.top.data)
    def display(self):
        if self.top is None:
                    print("Stack is empty")
        else:
                    temp=self.top
                    print("stack elements=")
                    while temp is not None:
                        print(temp.data)
                        temp=temp.next
s=stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
s.peek()
s.pop()
s.display()