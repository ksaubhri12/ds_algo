from Node import Node


def boundary_traversal(root: Node):
    if root is None:
        return []
    boundary_arr = [root.data]
    add_left_side(root.left, boundary_arr)
    add_leaf_nodes(root.left, boundary_arr)
    add_leaf_nodes(root.right, boundary_arr)
    add_right_reverse(root.right, boundary_arr)
    return boundary_arr


def add_leaf_nodes(root: Node, result_arr: []):
    if root is None:
        return result_arr
    add_leaf_nodes(root.left, result_arr)
    if root.left is None and root.right is None:
        result_arr.append(root.data)
        return result_arr
    add_leaf_nodes(root.right, result_arr)


def add_right_reverse(root: Node, result_arr: []):
    if root is None:
        return
    if root.right is not None:
        add_right_reverse(root.right, result_arr)
        result_arr.append(root.data)
    elif root.left is not None:
        add_right_reverse(root.left, result_arr)
        result_arr.append(root.data)


def add_left_side(root: Node, result_arr: []):
    if root is None:
        return
    if root.left is not None:
        result_arr.append(root.data)
        add_left_side(root.left, result_arr)
    elif root.right is not None:
        result_arr.append(root.data)
        add_left_side(root.right, result_arr)


if __name__ == '__main__':
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)

    node_1.left = node_2
    node_1.right = node_3

    print(boundary_traversal(node_1))

    node_1 = Node(1)
    print(boundary_traversal(node_1))
