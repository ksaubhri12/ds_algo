from Node import Node
from practice_450.binary_tree.BinaryTree import BinaryTree


def successor(root: Node):
    succ = root.right
    while succ.left is not None:
        succ = succ.left
    return succ


def deletion_of_node(root: Node, key):
    if root is None:
        return None

    if key > root.data:
        root.right = deletion_of_node(root.right, key)
    if key < root.data:
        root.left = deletion_of_node(root.left, key)

    if key == root.data:
        if root.right is None:
            temp = root.left
            root = None
            return temp

        if root.left is None:
            temp = root.right
            root = None
            return temp

        else:
            succ = successor(root)
            root.data, succ.data = succ.data, root.data
            root.right = deletion_of_node(root.right, key)

    return root


if __name__ == '__main__':
    node_1 = Node(5)
    node_2 = Node(3)
    node_3 = Node(6)

    node_1.left = node_2
    node_1.right = node_3

    node_4 = Node(2)
    node_5 = Node(4)

    node_2.left = node_4
    node_2.right = node_5

    node_6 = Node(7)
    node_3.right = node_6

    print('Current Binary Tree')
    BinaryTree(node_1).in_order_traversal()
    print('After Deletion')
    node_1 = deletion_of_node(node_1, 3)

    BinaryTree(node_1).in_order_traversal()

