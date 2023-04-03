from Node import Node
from practice_450.binary_tree.BinaryTree import BinaryTree


def bst_from_pre_order_traversal(pre_order: []):
    if len(pre_order) <= 0:
        return None

    root = Node(pre_order[0])
    index_for_right = check_first_greater_element(pre_order, root.data)
    if index_for_right == -1:
        root.right = None
        root.left = bst_from_pre_order_traversal(pre_order[1:])

    else:
        root.right = bst_from_pre_order_traversal(pre_order[index_for_right:])
        root.left = bst_from_pre_order_traversal(pre_order[1:index_for_right])

    return root


def check_first_greater_element(input_arr: [], key: int):
    n = len(input_arr)
    for i in range(0, n):
        if key < input_arr[i]:
            return i

    return -1


if __name__ == '__main__':
    head_node = bst_from_pre_order_traversal([8, 5, 1, 7, 10, 12])
    BinaryTree(head_node).in_order_traversal()
