class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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
    root.right = createBalanceBSTFromSortedArray(arr[mid+1:])
    return root


def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.data)
        printInorder(root.right)


arr = [1, 2, 3, 4, 5, 6, 7]
root = createBalanceBSTFromSortedArray(arr)
printInorder(root)
