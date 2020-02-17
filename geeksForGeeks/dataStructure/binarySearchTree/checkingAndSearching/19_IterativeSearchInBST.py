class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(node, data):
    if node is None:
        return Node(data)
    if data < node.data:
        node.left = insert(node.left, data)
    elif data > node.data:
        node.right = insert(node.right, data)
    return node


def iterativeSearch(root, key):
    while root:
        if root.data == key:
            break
        if root.data > key:
            root = root.left
            continue
        if root.data < key:
            root = root.right
            continue
    return root

root = None
root = insert(root, 50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)

print(iterativeSearch(root,20))