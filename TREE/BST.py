class node:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None


    def insert(self,data):
        if self.root is None:
            self.root=node(data)
        else:
            self._insert(data,self.root)

    def _insert(self,data,curr_node):
        if data<curr_node.data:
            if curr_node.left is None:
                curr_node.left=node(data)
            else:
                self._insert(data,curr_node.left)
        elif data>curr_node.data:
            if curr_node.right is None:
                curr_node.right=node(data)
            else:
                self._insert(data,curr_node.right)
        else:
            print("No duplicates are allowed")


    def find(self,data):
        if self.root:
            found=self._found(data,self.root)
            if found:
                print("Yes, it is present")
            else:
                print("It is absent")

    def _found(self,data,curr_node):
        if data<curr_node.data and curr_node.left:
            return self._found(data,curr_node.left)
        elif data>curr_node.data and curr_node.right:
            return self._found(data,curr_node.right)
        if data==curr_node.data:
            return True

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
bt=BST()
bt.insert(5)
bt.insert(6)
bt.insert(4)
bt.insert(1)

bt.find(5)
print(bt.check(bt.root))
