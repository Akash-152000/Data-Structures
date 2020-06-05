class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=node(data)

        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=new_node

    def print_list(self):
        if self.head==None:
            print("Empty list")

        temp=self.head
        while temp!=None:
            print(temp.data)
            temp=temp.next

    def prepend(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node


    def delete_node(self,key):
        curr_node=self.head
        if curr_node and curr_node.data==key:
            self.head=curr_node.next
            curr_node=None
            return

        prev=None
        while curr_node and curr_node.data!=key:
            prev=curr_node
            curr_node=curr_node.next

        if curr_node is None:
            print("NOT PRESENT")
            return
        prev.next=curr_node.next
        curr_node.next=None

        
    

ll=linkedList()
ll.append("A")
ll.append("B")
ll.append("C")
ll.prepend("D")
ll.delete_node("A")
ll.print_list()
