class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def kthLargestNode(root, k, i):
    if root is None or i[0] > k:
        return
    kthLargestNode(root.right, k, i)
    i[0] += 1
    if i[0] == k:
        print(root.data)
        return
    kthLargestNode(root.left, k, i)


def insert(node, key):
    if node is None:
        return Node(key)
    if node.data > key:
        node.left = insert(node.left, key)
    elif node.data < key:
        node.right = insert(node.right, key)
    return node

def kthLargest(root):
    i = [0]
    kthLargestNode(root,2,i)