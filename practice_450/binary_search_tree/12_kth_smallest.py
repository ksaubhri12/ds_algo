from Node import Node


def kth_smallest(root: Node, k):
    result_arr = [None]
    value_arr = [1]
    in_order_util(root, result_arr, value_arr, k)

    if result_arr[0] is None:
        return -1
    return result_arr[0]


def in_order_util(root: Node, result_arr: [], value_arr: [], k):
    if root is None:
        return

    in_order_util(root.left, result_arr, value_arr, k)
    if value_arr[0] == k:
        result_arr[0] = root.data
    value_arr[0] = value_arr[0] + 1
    in_order_util(root.right, result_arr, value_arr, k)


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
    print(kth_smallest(anode_1, 3))
