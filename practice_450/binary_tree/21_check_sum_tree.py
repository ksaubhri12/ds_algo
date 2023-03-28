from Node import Node


def check_sum_tree_main(root: Node):
    return check_sum_tree(root)[1]


def check_sum_tree(root: Node):
    if root is None:
        return [0, True]

    if root.left is None and root.right is None:
        return [root.data, True]

    left_node_val_check = check_sum_tree(root.left)
    right_node_val_check = check_sum_tree(root.right)

    sum_check = root.data == left_node_val_check[0] + right_node_val_check[0]

    if sum_check and left_node_val_check[1] and right_node_val_check[1]:
        return [root.data, True]
    else:
        return [root.data, False]


if __name__ == '__main__':
    node_1 = Node(3)
    node_2 = Node(1)
    node_3 = Node(2)

    node_1.left = node_2

    node_1.right = node_3

    print(check_sum_tree_main(node_1))
