class TernaryTree:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.middle = None
        self.right = None

    def preOrderTernaryTree(self,root):
        if root:
            print(root.data)
            self.preOrderTernaryTree(root.left)
            self.preOrderTernaryTree(root.middle)
            self.preOrderTernaryTree(root.right)
    
