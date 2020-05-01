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
        else:
            print("Traversal type not supported")

    def preorder(self,start,traversal):
        if start!=None:
            traversal+=str(start.data)+"-"
            traversal=self.preorder(start.left,traversal)
            traversal=self.preorder(start.right,traversal)
        return traversal
    


bt=Binary_tree(5)
bt.root.left=node(3)
bt.root.right=node(4)
bt.root.left.left=node(1)
bt.root.left.right=node(2)
print(bt.print_("Preorder"))
