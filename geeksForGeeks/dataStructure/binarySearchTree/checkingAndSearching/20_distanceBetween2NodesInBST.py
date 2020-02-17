class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(node, data):
    if node is None:
        return Node(data)
    if data < node.data:
        node.left = insert(node.left, data)
    elif data > node.data:
        node.right = insert(node.right, data)
    return node


def distanceFromRoot(root, x):
    if root.data == x:
        return 0
    if root.data > x:
        return 1 + distanceFromRoot(root.left, x)
    return 1 + distanceFromRoot(root.right, x)


def distanceBetweenTwoNodes(root, x, y):
    while root:
        if root.data < x and root.data < y:
            root = root.right
        elif root.data > x and root.data > y:
            root = root.left
        else:
            break
    return distanceFromRoot(root, x) + distanceFromRoot(root, y)

root = None
root = insert(root, 20)
insert(root, 10)
insert(root, 5)
insert(root, 15)
insert(root, 30)
insert(root, 25)
insert(root, 35)

print(distanceBetweenTwoNodes(root,5,35))