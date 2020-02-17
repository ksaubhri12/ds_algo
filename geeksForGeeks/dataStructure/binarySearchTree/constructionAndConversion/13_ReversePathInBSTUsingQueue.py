class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def reversePath(root, key, q):
    if q is None:
        q = []
    if root is None:
        return
    if root.data == key:
        q.insert(0, root.data)
        root.data = q[-1]
        q.pop()
        return
    elif root.data < key:
        q.insert(0, root.data)
        reversePath(root.right, key, q)
        root.data = q[-1]
        q.pop()
        return
    elif root.data > key:
        q.insert(0, root.data)
        reversePath(root.left, key, q)
        root.data = q[-1]
        q.pop()
        return
    return


def printInOrder(root):
    if root:
        printInOrder(root.left)
        print(root.data)
        printInOrder(root.right)


def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    if key > root.data:
        root.right = insert(root.right, key)
    return root


k = 80
q = []
root = None
root = insert(root, 50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)
printInOrder(root)

reversePath(root, k, q)
print("After")
printInOrder(root)
