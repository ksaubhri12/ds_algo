# Basic Tree traversal
# inorder - left, root, right
# post order - left, right, root
# pre order - root, left, right

from Node import Node


def tree_traversals(root: Node):
    in_order_result = []
    post_order_result = []
    pre_order_result = []
    in_order_traversal(root, in_order_result)
    post_order_traversal(root, post_order_result)
    pre_order_traversal(root, pre_order_result)
    return [in_order_result, post_order_result, pre_order_result]


def in_order_traversal(root: Node, result_arr: []):
    if root is None:
        return
    in_order_traversal(root.left, result_arr)
    result_arr.append(root.data)
    in_order_traversal(root.right, result_arr)


def post_order_traversal(root: Node, result_arr: []):
    if root is None:
        return
    post_order_traversal(root.left, result_arr)
    post_order_traversal(root.right, result_arr)
    result_arr.append(root.data)


def pre_order_traversal(root: Node, result_arr: []):
    if root is None:
        return
    result_arr.append(root.data)
    pre_order_traversal(root.left, result_arr)
    pre_order_traversal(root.right, result_arr)


if __name__ == '__main__':
    node_1 = Node(10)
    node_2 = Node(20)
    node_3 = Node(30)

    node_1.left = node_2
    node_1.right = node_3

    node_4 = Node(40)
    node_5 = Node(60)

    node_2.left = node_4
    node_2.right = node_5

    print(tree_traversals(node_1))
