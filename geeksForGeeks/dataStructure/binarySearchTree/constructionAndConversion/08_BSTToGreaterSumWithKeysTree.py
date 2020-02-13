class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def convertBSTToGreaterTree(root):
    treeSum = sumOfTree(root)
    i = [treeSum]
    inOrderTreeTraversal(root, i)


def sumOfTree(root):
    if root is None:
        return 0
    leftSum = sumOfTree(root.left)
    rightSum = sumOfTree(root.right)
    return root.data + leftSum + rightSum


def inOrderTreeTraversal(root, i):
    if root:
        inOrderTreeTraversal(root.left, i)
        root.data, i[0] = i[0], i[0] - root.data
        inOrderTreeTraversal(root.right, i)


def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.data)
        printInorder(root.right)

h
root = Node(5)
root.left = Node(2)
root.right = Node(13)
convertBSTToGreaterTree(root)
printInorder(root)
