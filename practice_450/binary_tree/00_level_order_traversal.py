from Node import Node


def level_order_traversal(root: Node):
    result_arr = []
    level_order_traversal_util(root, result_arr)
    return result_arr


def level_order_traversal_util(root: Node, result_arr):
    if root is None:
        return result_arr
    queue = []
    queue.append(root)
    while len(queue) > 0:
        result_node = queue.pop(0)
        result_arr.append(result_node.data)
        if result_node.left is not None:
            queue.append(result_node.left)

        if result_node.right is not None:
            queue.append(result_node.right)


if __name__ == '__main__':
    node_1 = Node(10)
    node_2  = Node(20)
    node_3 = Node(30)

    node_1.left = node_2
    node_1.right = node_3

    node_4 = Node(40)
    node_5 = Node(60)

    node_2.left = node_4
    node_2.right = node_5

    print(level_order_traversal(node_1))

