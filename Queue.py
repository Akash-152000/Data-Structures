from pythonds.basic import Queue
def hotPotato(names,num):
    q=Queue()
    for ele in names:
        q.enqueue(ele)
    while q.size()>1:
        for i in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()
    return q.dequeue()
li=list(map(str,input().split()))
num=int(input())
print(hotPotato(li,num))
