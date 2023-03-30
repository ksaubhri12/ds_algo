from Node import Node


def mirror_tree(root_1: Node, root_2: Node):
    if root_1 is None and root_2 is None:
        return True

    root_1_right = root_1.right
    root_1_left = root_1.left
    root_1_right_data = root_1_right.data if root_1_right is not None else -1
    root_1_left_data = root_1_left.data if root_1_left is not None else -1

    root_2_right = root_2.right
    root_2_left = root_2.left
    root_2_right_data = root_2_right.data if root_2_right is not None else -1
    root_2_left_data = root_2_left.data if root_2_left is not None else -1

    value_check = root_1_right_data == root_2_left_data and root_1_left_data == root_2_right_data
    return value_check and mirror_tree(root_1_right, root_2_left) and mirror_tree(root_1_left, root_2_right)

