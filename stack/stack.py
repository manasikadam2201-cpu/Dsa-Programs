stack=[]
max=5

def push(item):
    if len(stack)==max:
        print("stack Overflow")
    else:
        stack.append(item)
        print(item,"inserted")
        
def pop():
    if len(stack)==0:
        print("stack Underflow")
    else:
        item=stack.pop
        print("Deleted element:",item)
        
def peek():
    if len(stack)==0:
        print("Stack is Empty")
    else:
        print("top element:",stack[-1])
        
def display():
    if len(stack)==0:
            print("Stack is Empty")
    else:
            print("top element:",stack[::-1])
    
        
push(10)
push(20)
push(30)
display()
peek()
pop()
display()


