from Node import Node
from BinaryTree import BinaryTree


def mirror_tree(root: Node):
    if root is None:
        return root

    root.left, root.right = root.right, root.left
    mirror_tree(root.left)
    mirror_tree(root.right)

    return root


if __name__ == '__main__':
    node_1 = Node(10)
    node_2 = Node(20)
    node_3 = Node(30)

    node_1.left = node_2
    node_1.right = node_3

    node_4 = Node(40)
    node_5 = Node(60)

    node_2.left = node_4
    node_2.right = node_5

    print('Current Binary Tree')
    BinaryTree(node_1).in_order_traversal()
    print('Mirroring Binary Tree')
    new_root = mirror_tree(node_1)
    BinaryTree(new_root).in_order_traversal()

