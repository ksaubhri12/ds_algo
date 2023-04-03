from Node import Node


def median_bst(root: Node):
    count_arr = [0]
    in_order_count_util(root, count_arr)
    n = count_arr[0]
    if n % 2 == 0:
        result_arr = [None]
        value_arr = [1]
        in_order_smallest(root, result_arr, value_arr, n // 2)
        element_1 = result_arr[0]
        result_arr = [None]
        value_arr = [1]
        in_order_smallest(root, result_arr, value_arr, n // 2 + 1)
        element_2 = result_arr[0]
        median = (element_1 + element_2) // 2
    else:
        result_arr = [None]
        value_arr = [1]
        in_order_smallest(root, result_arr, value_arr, (n + 1) // 2)
        median = result_arr[0]

    return median


def in_order_count_util(root: Node, count_arr: []):
    if root is None:
        return
    in_order_count_util(root.left, count_arr)
    count_arr[0] = count_arr[0] + 1
    in_order_count_util(root.right, count_arr)


def in_order_smallest(root: Node, result_arr: [], value_arr: [], k):
    if root is None:
        return

    in_order_smallest(root.left, result_arr, value_arr, k)
    if value_arr[0] == k:
        result_arr[0] = root.data
    value_arr[0] = value_arr[0] + 1
    in_order_smallest(root.right, result_arr, value_arr, k)


if __name__ == '__main__':
    anode_1 = Node(8)
    anode_2 = Node(2)
    anode_3 = Node(18)
    anode_4 = Node(1)
    anode_5 = Node(22)
    anode_1.left = anode_2
    anode_1.right = anode_3

    anode_2.left = anode_4
    anode_3.right = anode_5

    print(median_bst(anode_1))
