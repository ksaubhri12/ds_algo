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

def kthLargest(root,k):
    i = [0]
    kthLargestNode(root,k,i)

root = None
root = insert(root, 50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)

for k in range(1,8):
    kthLargest(root,k)