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
        else:
            return(self.postorder(bt.root,""))

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
    

bt=Binary_tree(5)
bt.root.left=node(3)
bt.root.right=node(4)
bt.root.left.left=node(1)
bt.root.left.right=node(2)
bt.root.right.left=node(6)
bt.root.right.right=node(7)
print(bt.print_("Preorder"))
print(bt.print_("Inorder"))
print(bt.print_("Postorder"))
