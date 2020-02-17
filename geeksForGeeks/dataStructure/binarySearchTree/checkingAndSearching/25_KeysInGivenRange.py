class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(node, key):
    if node is None:
        return Node(key)
    if node.data > key:
        node.left = insert(node.left, key)
    if node.data < key:
        node.right = insert(node.right, key)
    return node


def printNearNodes(root, k1, k2):
    if root:
        if k2 > root.data:
            printNearNodes(root.right, k1, k2)

        if k1 <= root.data <= k2:
            print(root.data)

        if root.data > k1:
            printNearNodes(root.left, k1, k2)
