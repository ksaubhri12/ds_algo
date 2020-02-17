class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def lcaIterative(root, n1, n2):
    while root:
        if root.data < n1 and root.data < n2:
            root = root.right
        elif root.data > n1 and root.data > n2:
            root = root.left
        else:
            break
    return root.data


root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

print(lcaIterative(root, 10, 14))
