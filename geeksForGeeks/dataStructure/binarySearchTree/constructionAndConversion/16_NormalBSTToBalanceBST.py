class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def constructBalanceBSTFromBST(root):
    arr = []
    inOrderTraversalUtil(root, arr)
    root = createBalanceBSTFromSortedArray(arr)
    return root


def inOrderTraversalUtil(root, arr):
    if root:
        inOrderTraversalUtil(root.left, arr)
        arr.append(root.data)
        inOrderTraversalUtil(root.right, arr)


def createBalanceBSTFromSortedArray(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        root = Node(arr[0])
        return root
    high = len(arr) - 1
    low = 0
    mid = high + (low - high) / 2
    mid = int(mid)
    root = Node(arr[mid])
    root.left = createBalanceBSTFromSortedArray(arr[:mid])
    root.right = createBalanceBSTFromSortedArray(arr[mid + 1:])
    return root


def printInOrder(root):
    if root:
        printInOrder(root.left)
        print(root.data)
        printInOrder(root.right)


root = Node(10)
root.left = Node(8)
root.left.left = Node(7)
root.left.left.left = Node(6)
root.left.left.left.left = Node(5)

root = constructBalanceBSTFromBST(root)
printInOrder(root)
