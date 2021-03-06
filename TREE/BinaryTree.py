class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Binary_tree:
    def __init__(self,data):
        self.root=node(data)

    def print_(self,traverse):
        if traverse=="Preorder":
            return self.preorder(bt.root,"")
        elif traverse=="Inorder":
            return self.inorder(bt.root,"")
        elif traverse=="Levelorder":
            qu=[bt.root]
            return self.levelorder(qu,"")
        elif traverse=="ReverseLevelOrder":
            qu=[bt.root]
            return self.reverseLevel(qu,"")
        elif traverse=="SumOfEdges":
            sum=0
            return self.sum_edges(bt.root,sum)
        elif traverse=="Height":
            return self.height(bt.root)
        elif traverse=="Size":
            count=0
            return self.size(bt.root,count)
        elif traverse=="Postorder":
            return (self.postorder(bt.root,""))

    def preorder(self,start,traversal):
        """root<left<right"""
        if start!=None:
            traversal+=str(start.data)+"-"
            traversal=self.preorder(start.left,traversal)
            traversal=self.preorder(start.right,traversal)
        return traversal
    
    def inorder(self,start,traversal):
        """left<root<right"""
        if start:
            traversal=self.inorder(start.left,traversal)
            traversal+=str(start.data)+"-"
            traversal=self.inorder(start.right,traversal)
        return traversal

    def postorder(self,start,traversal):
        """"left<right<root"""
        if start:
            traversal=self.postorder(start.left,traversal)
            traversal=self.postorder(start.right,traversal)
            traversal+=str(start.data)+"-"
        return traversal
    
    def levelorder(self,qu,traversal):
        while len(qu)!=0:
            m=qu.pop()
            traversal+=str(m.data)+"-"
            if m.left!=None:
                qu.insert(0,m.left)
            if m.right!=None:
                qu.insert(0,m.right)
        return traversal
    
    def reverseLevel(self,qu,traversal):
        while len(qu)!=0:
            m=qu.pop()
            traversal=str(m.data)+"-"+traversal
            if m.left!=None:
                qu.insert(0,m.left)
            if m.right!=None:
                qu.insert(0,m.right)
        return traversal
         
    def sum_edges(self,start,sum):
        """root<left<right"""
        if start!=None:
            sum+=start.data
            sum=self.sum_edges(start.left,sum)
            sum=self.sum_edges(start.right,sum)
        return sum

    def height(self,start):
        if start==None:
            return -1
        left=self.height(start.left)
        right=self.height(start.right)
        return 1+max(left,right)

    def size(self,start,count):
        if start:
            count=self.size(start.left,count)
            count+=1
            count=self.size(start.right,count)
        return count

    def check(self,start):
        ans=True
        if start==None:
            return False
        if start.left:
            if start.left.data<start.data:
                ans=True
                self.check(start.left)
            else:
                return False
        if start.right:
            if start.right.data>start.data:
                ans=True
                self.check(start.right)
            else:
                return False
        return ans
         


bt=Binary_tree(5)
bt.root.left=node(3)
bt.root.right=node(8)
bt.root.left.left=node(1)
bt.root.left.right=node(2)
bt.root.right.left=node(6)
bt.root.right.right=node(7)
bt.root.right.left.left=node(4)
bt.root.right.right.right=node(9)

#                 5
#             /      \
#           /          \
#          3             8
#       /     \       /     \
#      1       2     6       7
#                   /  \ 
#                  4    9

#Preorder:5-3-1-2-4-6-8-7-9-

#Inoreder:1-3-2-5-8-6-4-7-9-

#Postorder:1-2-3-8-6-9-7-4-5-

#Levelorder:5-3-4-1-2-6-7-8-9-

#Reverseorder:9-8-7-6-2-1-4-3-5-

#sum:45

#Height:3

#Size:9

print(bt.print_("Preorder"))
print(bt.print_("Inorder"))
print(bt.print_("Postorder"))
print(bt.print_("Levelorder"))
print(bt.print_("ReverseLevelOrder"))
print(bt.print_("SumOfEdges"))
print(bt.print_("Height"))
print(bt.print_("Size"))
print(bt.check(bt.root))
