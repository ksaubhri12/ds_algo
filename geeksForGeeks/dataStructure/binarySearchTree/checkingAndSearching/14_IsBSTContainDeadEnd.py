class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def insert(node,key):
    if node is None:
        return Node(key)
    if node.data > key:
        node.left = insert(node.left,key)
    if node.data < key:
        node.right = insert(node.right,key)
    return node

def isDeadEnd(root):
    pass