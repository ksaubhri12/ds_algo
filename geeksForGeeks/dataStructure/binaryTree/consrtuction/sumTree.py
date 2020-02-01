class Node:

    def __init__(self,data = None):
        self.data = data
        self.left = None
        self.right = None

    def sumToTree(self,node):

        if node is None:
            return 0
        oldValue = node.data
        node.data = self.sumToTree(node.left) + self.sumToTree(node.right)

        return node.data + oldValue

