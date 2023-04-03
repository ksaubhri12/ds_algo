from Node import Node


def check_bst(root: Node):
    prev_arr = [None]
    result_arr = [True]
    check_bst_util(root, prev_arr, result_arr)
    return result_arr[0]


def check_bst_util(root: Node, prev_arr: [], result_arr: []):
    if root is None:
        return
    check_bst_util(root.left, prev_arr, result_arr)

    if prev_arr[0] is None:
        prev_arr[0] = root
    elif prev_arr[0] is not None and root.data <= prev_arr[0].data:
        result_arr[0] = False
    elif prev_arr[0] is not None and root.data > prev_arr[0].data:
        prev_arr[0] = root

    check_bst_util(root.right, prev_arr, result_arr)


if __name__ == '__main__':
    node_1 = Node(2)
    node_2 = Node(1)
    node_3 = Node(3)

    node_1.left = node_2
    node_1.right = node_3
    print(check_bst(node_1))
