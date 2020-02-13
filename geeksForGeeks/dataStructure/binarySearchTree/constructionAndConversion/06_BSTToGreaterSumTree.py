class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def BSTtoGreaterSumTree(root):
    totalSum = sumOfTree(root)
    i = [totalSum]
    inOrderTraversalUtil(root, i)


def sumOfTree(root):
    if root is None:
        return 0
    leftSum = sumOfTree(root.left)
    rightSum = sumOfTree(root.right)
    return root.data + leftSum + rightSum


def inOrderTraversalUtil(root, i):
    if root:
        inOrderTraversalUtil(root.left, i)
        oldValue = root.data
        root.data = i[0] - oldValue
        i[0] = root.data
        inOrderTraversalUtil(root.right, i)


def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.data)
        printInorder(root.right)



root = Node(11)
root.left = Node(2)
root.right = Node(29)
root.left.left = Node(1)
root.left.right = Node(7)
root.right.right = Node(40)
root.right.left = Node(15)
root.right.right.left = Node(35)
BSTtoGreaterSumTree(root)
printInorder(root)
