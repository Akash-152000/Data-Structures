class stack:
    def __init__(self):
        self.stk=[]
    def push(self,n):
        self.stk.append(n)
    def pop(self):
        a=self.stk[-1]
        self.stk.pop()
        return a

di={"/":4,"*":3,"+":2,"-":1,"(":0}


st=stack()
answer=[]
exp=input()
exp1=list(exp)
for ele in exp1:
    if ele=="(":
        st.push(ele)
    elif ele in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        answer.append(ele)
    elif ele in "*/+-":
        if len(st.stk)==0:
            st.push(ele)
        elif di[st.stk[-1]]>di[ele]:
            answer.append(st.pop())
            st.push(ele)
        else:
            st.push(ele)
    elif ele==")":
        if st.stk[-1]!=")":
            answer.append(st.pop())
        else:
            st.pop()

while True:
    if len(st.stk)==0:
        break
    else:
        answer.append(st.pop())
str1=""
for ele in answer:
    if ele=="(":
        pass
    else:
        str1+=ele
print(str1)

                      
                      
                      

            
