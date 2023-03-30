from Node import Node


def check_sum(root: Node):
    return check_sum_tree_util(root)[0]


def check_sum_tree_util(root: Node):
    if root is None:
        return [True, 0]

    if root.left is None and root.right is None:
        return [True, root.data]

    left_tree_check = check_sum_tree_util(root.left)
    right_tree_check = check_sum_tree_util(root.right)

    value_check = root.data == left_tree_check[1] + right_tree_check[1] and left_tree_check[0] and right_tree_check[0]
    return [value_check, root.data + left_tree_check[1] + right_tree_check[1]]


if __name__ == '__main__':
    node_1 = Node(3)
    node_2 = Node(1)
    node_3 = Node(2)

    node_1.left = node_2
    node_1.right = node_3

    print(check_sum(node_1))

    node_1 = Node(40)
    node_2 = Node(20)
    node_3 = Node(30)
    node_4 = Node(10)
    node_5 = Node(10)

    node_1.left = node_2
    node_1.right = node_3
    node_2.left = node_4
    node_2.right = node_5

    print(check_sum(node_1))
