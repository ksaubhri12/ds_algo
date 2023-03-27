from Node import Node


def pre_order_traversal(root: Node):
    result_arr = []
    pre_order_traversal_util(root, result_arr)
    return result_arr


def pre_order_traversal_util(root: Node, result_arr: []):
    if root is None:
        return
    result_arr.append(root.data)
    pre_order_traversal_util(root.left, result_arr)
    pre_order_traversal_util(root.right, result_arr)


if __name__ == '__main__':
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)

    node_1.left = node_2
    node_1.right = node_3

    node_4 = Node(4)
    node_5 = Node(5)

    node_2.left = node_4
    node_2.right = node_5

    print(pre_order_traversal(node_1))
