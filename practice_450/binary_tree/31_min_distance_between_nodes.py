from Node import Node


def min_distance(root: Node, n1, n2):
    lca_node = lca(root, n1, n2)
    n1_dist = distance_from_lca(lca_node, n1)
    n2_dist = distance_from_lca(lca_node, n2)
    return n1_dist + n2_dist - 2


def distance_from_lca(root: Node, value: int):
    if root is None:
        return 0
    if root.data == value:
        return 1
    left_check = distance_from_lca(root.left, value)
    right_check = distance_from_lca(root.right, value)
    if left_check == 0 and right_check == 0:
        return 0
    return left_check + right_check + 1


def lca(root: Node, n1: int, n2: int):
    if root is None:
        return None

    if root.data == n1 or root.data == n2:
        return root

    left_check = lca(root.left, n1, n2)
    right_check = lca(root.right, n1, n2)

    if left_check is not None and right_check is not None:
        return root
    elif left_check is None:
        return right_check
    else:
        return left_check
