from Node import Node


def lca_binary_tree(root: Node, n1, n2):
    if root is None:
        return None

    if root.data == n1 or root.data == n2:
        return root.data

    left_check = lca_binary_tree(root.left, n1, n2)
    right_check = lca_binary_tree(root.right, n1, n2)

    if left_check is not None and right_check is not None:
        return root.data
    elif left_check is None:
        return right_check
    else:
        return left_check


if __name__ == '__main__':
    node_1 = Node(5)
    node_2 = Node(2)
    node_3 = Node(8)
    node_4 = Node(4)
    node_5 = Node(3)

    node_1.left = node_2
    node_2.left = node_3
    node_2.right = node_4
    node_3.left = node_5

    print(lca_binary_tree(node_1, 3, 4))

    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)

    node_1.left = node_2
    node_1.right = node_3
    print(lca_binary_tree(node_1, 2, 3))

    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)

    node_1.left = node_2
    node_1.right = node_3

    node_4 = Node(4)
    node_5 = Node(5)
    node_6 = Node(6)

    node_7 = Node(7)

    node_2.left = node_4
    node_3.left = node_5
    node_3.right = node_6

    node_4.right = node_7
    print(lca_binary_tree(node_1, 7, 5))
    print(lca_binary_tree(node_1, 4, 2))
