from Node import Node


def get_lca(root: Node, n1, n2):
    if n1 <= n2:
        return get_lca_util(root, n1, n2)
    else:
        return get_lca_util(root, n2, n1)


def get_lca_util(root: Node, start, end):
    if root is None:
        return None

    if start <= root.data <= end:
        return root

    elif end < root.data:
        return get_lca_util(root.left, start, end)

    else:
        return get_lca_util(root.right, start, end)
