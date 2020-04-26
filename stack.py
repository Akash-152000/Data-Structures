class stack:
    def __init__(self):
        self.stk=[]
    def push(self,x):
        self.stk.append(x)
    def pop(self):
        if len(self.stk)==0:
            return -1
        else:
            self.stk.pop()
    def peep(self):
        n=len(self.stk)
        return self.stk[n-1]
    def display(self):
        return self.stk

st=stack()
while True:
    print("1:PUSH")
    print("2:POP")
    print("3:PEEP")
    print("4:DISPLAY")
    print("5:EXIT")
    ch=int(input())
    if ch==1:
        num=int(input("Enter the number to be pushed:"))
        st.push(num)
    elif ch==2:
        st.pop()
    elif ch==3:
        print(st.peep())
    elif ch==4:
        print(st.display())
    else:
        break
