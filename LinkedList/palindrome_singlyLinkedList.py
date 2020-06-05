class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlyLinkedList:
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


    def print(self):
        if self.head==None:
            print("Empty list")
        temp=self.head
        while temp!=None:
            print(temp.data)
            temp=temp.next

    def palindrome(self):
        s=""
        if self.head==None:
            print("Empty List")
        temp=self.head
        while temp.next!=None:
            s+=temp.data
            temp=temp.next
        if s==s[::-1]:
            print("Yes,it is a palondrome")
        else:
            print("No,it is not a palindrome")

sl=singlyLinkedList()
sl.append("B")
sl.append("A")
sl.append("B")
sl.append("A")
sl.print()
sl.palindrome()
