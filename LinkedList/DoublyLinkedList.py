class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        if self.head == None:
            new_node=node(data)
            self.head=new_node
            new_node.prev=None
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            new_node=node(data)
            new_node.prev=temp
            temp.next=new_node
            new_node.next=None
            
    def prepend(self,data):
        if self.head==None:
            new_node=node(data)
            new_node.prev=None
        else:
            new_node=node(data)
            new_node.next=self.head
            self.head.prev=new_node
            new_node.prev=None
            self.head=new_node

        

    def print_(self):
        temp=self.head
        while temp!=None:
            print(temp.data)
            temp=temp.next


dl=DoublyLinkedList()
dl.append(1)
dl.append(2)
dl.append(3)
dl.append(4)
dl.prepend(5)
dl.print_()
