class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def convertFromBinaryTreeToBST(root):
    tempArr = []
    inOrderTraversal(root, tempArr)
    tempArr.sort()
    i = [0]
    inOrderTraversalUtil(root, tempArr, i)
    return root


def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.data)
        printInorder(root.right)


def inOrderTraversal(root, arr):
    if root:
        inOrderTraversal(root.left, arr)
        arr.append(root.data)
        inOrderTraversal(root.right, arr)


def inOrderTraversalUtil(root, arr, i):
    if root:
        inOrderTraversalUtil(root.left, arr, i)
        root.data = arr[i[0]]
        i[0] += 1
        inOrderTraversalUtil(root.right, arr, i)

root = Node(10)
root.left = Node(30)
root.right = Node(15)
root.left.left = Node(20)
root.right.right= Node(5)
convertFromBinaryTreeToBST(root)
printInorder(root)