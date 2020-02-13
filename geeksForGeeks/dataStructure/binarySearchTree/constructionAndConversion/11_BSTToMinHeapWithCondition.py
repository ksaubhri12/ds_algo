class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def constructMinHeapFromBST(root):
    arr = []
    inOrderTraversalUtil(root, arr)
    i = [0]
    preOrderTraversalUtil(root,arr,i)


def inOrderTraversalUtil(root, arr):
    if root:
        inOrderTraversalUtil(root.left, arr)
        arr.append(root.data)
        inOrderTraversalUtil(root.right, arr)


def preOrderTraversalUtil(root, arr, i):
    if root:
        root.data = arr[i[0]]
        i[0] += 1
        preOrderTraversalUtil(root.left, arr, i)
        preOrderTraversalUtil(root.right, arr, i)


def printInOrder(root):
    if root:
        printInOrder(root.left)
        print(root.data)
        printInOrder(root.right)


def printPreOrder(root):
    if root:
        print(root.data)
        printPreOrder(root.left)
        printPreOrder(root.right)


root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)
print("Before conversion in order")
printInOrder(root)
constructMinHeapFromBST(root)
print("After conversion In order")
printInOrder(root)
print("After conversion preOrder")
printPreOrder(root)
