from Node import Node
from practice_450.linkedlist.LinkedList import LinkedList


def binary_tree_dll(root: Node):
    head = [None]
    prev = [None]
    binary_tree_dll_util(root, head, prev)
    return head[0]


def binary_tree_dll_util(root: Node, head_arr, prev_arr):
    if root is None:
        return None

    binary_tree_dll_util(root.left, head_arr, prev_arr)
    if head_arr[0] is None:
        head_arr[0] = root
        prev_arr[0] = root
    else:
        prev_arr[0].right = root
        root.left = prev_arr[0]
        prev_arr[0] = root
    binary_tree_dll_util(root.right, head_arr, prev_arr)


if __name__ == '__main__':
    node_1 = Node(10)
    node_2 = Node(12)
    node_3 = Node(15)

    node_1.left = node_2
    node_1.right = node_3

    node_4 = Node(25)
    node_5 = Node(30)
    node_6 = Node(36)

    node_2.left = node_4
    node_2.right = node_5

    node_3.left = node_6
    head_node = binary_tree_dll(node_1)
    LinkedList(head_node).print_linked_list_tree()
