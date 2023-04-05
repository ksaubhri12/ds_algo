from Node import Node


def check_dead_end(root: Node):
    result_arr = [False]
    in_order_util(root, 1, float('inf'), result_arr)
    return result_arr[0]


def in_order_util(root: Node, lowest_range, highest_range, result_arr: []):
    if root is None:
        return

    in_order_util(root.left, lowest_range, root.data - 1, result_arr)
    if root.left is None and root.right is None:
        if lowest_range == root.data and highest_range == root.data:
            result_arr[0] = True

    in_order_util(root.right, root.data + 1, highest_range, result_arr)


if __name__ == '__main__':
    node_1 = Node(8)
    node_2 = Node(5)

    node_3 = Node(9)
    node_1.left = node_2
    node_1.right = node_3

    node_4 = Node(2)
    node_5 = Node(7)
    node_2.left = node_4
    node_2.right = node_5

    node_6 = Node(1)
    node_4.left = node_6
    print(check_dead_end(node_1))

    node_1 = Node(8)
    node_2 = Node(7)
    node_3 = Node(10)

    node_1.left = node_2
    node_1.right = node_3

    node_4 = Node(2)
    node_5 = Node(9)
    node_6 = Node(13)
    node_2.left = node_4
    node_3.left = node_5
    node_3.right = node_6
    print(check_dead_end(node_1))
