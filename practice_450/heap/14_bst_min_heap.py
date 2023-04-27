class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def bst_min_heap(root: Node):
    in_order_arr = []
    in_order_util(root, in_order_arr)
    n = len(in_order_arr)
    setting_tree(root, in_order_arr, n, 0)
    in_order_arr = []
    pre_order_traversal(root, in_order_arr)
    return in_order_arr


def in_order_util(root: Node, result_arr: []):
    if root is None:
        return
    in_order_util(root.left, result_arr)
    result_arr.append(root.data)
    in_order_util(root.right, result_arr)


def pre_order_traversal(root: Node, result_arr: []):
    if root is None:
        return
    result_arr.append(root.data)
    pre_order_traversal(root.left, result_arr)
    pre_order_traversal(root.right, result_arr)


def setting_tree(root: Node, result_arr: [], n, index):
    if root is None:
        return

    if index >= n:
        return
    root.data = result_arr[index]
    left = 2 * index + 1
    right = 2 * index + 2

    if left < n:
        setting_tree(root.left, result_arr, n, left)
    if right < n:
        setting_tree(root.right, result_arr, n, right)


if __name__ == '__main__':
    node_1 = Node(4)
    node_2 = Node(2)
    node_3 = Node(6)

    node_1.left = node_2
    node_1.right = node_3

    # print(bst_min_heap(node_1))

    node_1 = Node(8)
    node_2 = Node(5)
    node_3 = Node(10)

    node_1.left = node_2
    node_1.right = node_3

    node_4 = Node(2)
    node_5 = Node(6)
    node_2.left = node_4
    node_2.right = node_5

    node_6 = Node(7)
    node_5.right = node_6
    print(bst_min_heap(node_1))
