class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class circularLinkedList:
    def __init__(self):
        self.head=None

    def append_(self,data):
        if not self.head:
            self.head=node(data)
            self.head.next=self.head
            return
        
        new_node=node(data)
        temp=self.head
        while temp.next!=self.head:
            temp=temp.next
        temp.next=new_node
        new_node.next=self.head

    def prepend_(self,data):
        if not self.head:
            self.head=node(data)
            self.head.next=self.head
            return
        new_node=node(data)
        temp=self.head
        while temp.next!=self.head:
            temp=temp.next
        temp.next=new_node
        new_node.next=self.head
        self.head=new_node

    def delete_(self,key):
        if self.head.data==key:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=self.head.next
            self.head=self.head.next
        else:
            temp=self.head
            prev=None
            while temp.next!=self.head:
                prev=temp
                temp=temp.next
                if temp.data==key:
                    prev.next=temp.next
                    temp=temp.next
                
        
    def print_(self):
        if self.head==None:
            print("Empty list")
            return
        temp=self.head
        print(temp.data)
        while temp.next!=self.head:
            temp=temp.next
            print(temp.data)


cl=circularLinkedList()
cl.append_("A")
cl.append_("B")
cl.append_("C")
cl.append_("D")
cl.prepend_("E")
cl.prepend_("F")
cl.append_("G")
cl.print_()
print()
print()
cl.delete_("C")
cl.print_()
            
            
