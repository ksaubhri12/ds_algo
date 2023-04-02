from Node import Node


def print_k_sum_path(root: Node, path_stack: [], k):
    if root is None:
        return
    path_stack.append(root.data)
    print_k_sum_path(root.left, path_stack, k)
    print_k_sum_path(root.right, path_stack, k)

    sum_value = 0
    n = len(path_stack)
    for i in reversed(range(0, n)):
        sum_value = sum_value + path_stack[i]
        if sum_value == k:
            print(path_stack[i:])

    path_stack.pop()


def print_k_sum(root: Node, k):
    path_stack = []
    print_k_sum_path(root, path_stack, k)


if __name__ == '__main__':
    node_1 = Node(1)
    node_2 = Node(3)
    node_3 = Node(-1)

    node_1.left = node_2
    node_1.right = node_3

    node_4 = Node(2)
    node_5 = Node(1)
    node_6 = Node(4)
    node_7 = Node(5)

    node_2.left = node_4
    node_2.right = node_5

    node_3.left = node_6
    node_3.right = node_7

    node_8 = Node(1)
    node_9 = Node(1)
    node_10 = Node(2)
    node_11 = Node(6)

    node_5.left = node_8
    node_6.left = node_9
    node_6.right = node_10
    node_7.right = node_11

    print_k_sum(node_1, 5)
