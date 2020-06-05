class queue:
    def __init__(self):
        self.que=[]
    def enqueue(self,n):
        self.que.insert(0,n)
    def dequeue(self):
        if len(self.que)==0:
            print("EMPTY")
        else:
            self.que.pop()
    def display(self):
        return self.que
    def isEmpty(self):
        if self.que==[]:
            return True
        else:
            return False
q=queue()
while True:
    print("1:ENQUEUE")
    print("2:DEQUEUE")
    print("3:CHECK IF EMPTY")
    print("4:DISPLAY")
    print("5:EXIT")
    n=int(input())
    if n==1:
        q.enqueue(input("Enter the element to be enqueued:"))
    elif n==2:
        q.dequeue()
    elif n==3:
        print(q.isEmpty())
    elif n==4:
        print(q.display())
    else:
        break
    
