from Node import Node
from BinaryTree import BinaryTree


def tree_from_in_order_pre_order(in_order: [], pre_order: []):
    if len(in_order) == 0:
        return None

    if len(in_order) == 1:
        return Node(in_order[0])

    root_data = pre_order[0]
    root_index = find_index_in_in_order_arr(root_data, in_order)
    root_node = Node(root_data)
    root_node.left = tree_from_in_order_pre_order(in_order[0:root_index], pre_order[1: root_index+1])
    root_node.right = tree_from_in_order_pre_order(in_order[root_index + 1:], pre_order[root_index+1:])
    return root_node


def find_index_in_in_order_arr(root_node: int, in_order: []):
    for i in range(0, len(in_order)):
        if in_order[i] == root_node:
            return i

    return -1


if __name__ == '__main__':
    head_node = tree_from_in_order_pre_order([3, 1, 4, 0, 5, 2], [0, 1, 3, 4, 2, 5])
    BinaryTree(head_node).post_order()

