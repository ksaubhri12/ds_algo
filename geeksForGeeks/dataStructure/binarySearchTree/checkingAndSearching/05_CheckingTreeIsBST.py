class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


INT_MIN = float("-inf")
INT_MAX = float("inf")


def checkIfTreeIsBST(root):
    return checkUtil(root, INT_MIN, INT_MAX)


def checkUtil(node, min, max):

    if node is None:
        return True
    if node.data < min or node.data > max:
        return False

    return checkUtil(node.left, min, node.data) and checkUtil(node.right, node.data, max)

root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

print(checkIfTreeIsBST(root))

