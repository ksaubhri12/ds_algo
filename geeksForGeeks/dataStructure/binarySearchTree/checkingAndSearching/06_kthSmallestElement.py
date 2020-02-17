class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def kSmallestElement(root, n):
    stack = []
    inOrderUtil(root, stack)
    return stack[n - 1]


def inOrderUtil(root, stack):
    if root:
        inOrderUtil(root.left, stack)
        stack.append(root.data)
        inOrderUtil(root.right, stack)
