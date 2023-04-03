from Node import Node
from practice_450.binary_tree.BinaryTree import BinaryTree


def normal_bst_balance_bst(root: Node):
    in_order_arr = []
    in_order_util(root, in_order_arr)
    return create_bst_from_in_order(in_order_arr)


def in_order_util(root: Node, in_order_arr: []):
    if root is None:
        return

    in_order_util(root.left, in_order_arr)
    in_order_arr.append(root.data)
    in_order_util(root.right, in_order_arr)


def create_bst_from_in_order(in_order_arr: []):
    if len(in_order_arr) <= 0:
        return None

    start = 0
    end = len(in_order_arr) - 1
    middle = start + (end - start) // 2
    root = Node(in_order_arr[middle])
    root.left = create_bst_from_in_order(in_order_arr[start:middle])
    root.right = create_bst_from_in_order(in_order_arr[middle+1:])
    return root


if __name__ == '__main__':
    node_1 = Node(30)
    node_2 = Node(20)
    node_3 = Node(10)

    node_1.left = node_2
    node_2.left = node_3

    print('Current Binary Tree Inorder and post order')
    BinaryTree(node_1).in_order_traversal()
    BinaryTree(node_1).post_order()

    print('After Balance inorder and post order')
    new_root_node = normal_bst_balance_bst(node_1)
    BinaryTree(new_root_node).in_order_traversal()
    BinaryTree(new_root_node).post_order()

