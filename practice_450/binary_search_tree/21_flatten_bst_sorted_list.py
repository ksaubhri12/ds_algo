from Node import Node
from practice_450.binary_tree.BinaryTree import BinaryTree


def flatten_bst(root: Node):
    prev_arr = [None]
    head_arr = [None]
    in_order_util(root, prev_arr, head_arr)
    return head_arr[0]


def in_order_util(root: Node, prev_arr: [], head_arr: []):
    if root is None:
        return

    in_order_util(root.left, prev_arr, head_arr)

    if head_arr[0] is None:
        head_arr[0] = root
        prev_arr[0] = root

    else:
        prev_arr[0].right = root
        prev_arr[0].left = None
        prev_arr[0] = root

    in_order_util(root.right, prev_arr, head_arr)


if __name__ == '__main__':
    node_1 = Node(5)
    node_2 = Node(3)
    node_3 = Node(7)

    node_1.left = node_2
    node_1.right = node_3

    node_4 = Node(2)
    node_5 = Node(4)
    node_6 = Node(6)
    node_7 = Node(8)

    node_2.left = node_4
    node_2.right = node_5

    node_3.left = node_6
    node_3.right = node_7

    print('Current Binary Tree')
    BinaryTree(node_1).pre_order()
    print('After Flattening it')
    new_head_node = flatten_bst(node_1)
    BinaryTree(new_head_node).pre_order()
