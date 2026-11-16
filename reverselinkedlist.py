class Node:
 def __init__(self,data): 
  self.data=data
  self.next=Null 
  
  #function to reverse a linked list
  def reverse_linkedlist(head):
      prev=None
      current=head
      while current is not None:
        next_node=current.next   
      current.next=prev
      prev=current
      current=next_node
      return prev
      current=next_node
      return prev
  
  #function to display
  def display(head):
      current=head
      while current is not None:
       print (current.data)
       current=current.next
       print("Null")
       
 #create alist
  head=node(10)
  head.next=node(20)
  head.next.next=node(30)
  head.next.next.next=node(40)
  print("original linked list")
  display(head)
  head=reverse_linkedlist(head)
  print("reversed linked list")
  display(head)
       
            
          
      
