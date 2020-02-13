class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def smallerKeyTree(root):
    sum = [0]
    inOrderTraversal(root, sum)


def inOrderTraversal(root, sum):
    if root:
        inOrderTraversal(root.left, sum)

        sum[0] = sum[0] + root.data
        root.data = sum[0]
        inOrderTraversal(root.right, sum)


def printInOrder(root):
    if root:
        printInOrder(root.left)
        print(root.data)
        printInOrder(root.right)


def printPostOrder(root):
    if root:
        printPostOrder(root.left)
        printPostOrder(root.right)
        print(root.data)


root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)
printPostOrder(root)

#
# root = Node(9)
# root.left = Node(6)
# root.right = Node(15)
# smallerKeyTree(root)
# printInOrder(root)
