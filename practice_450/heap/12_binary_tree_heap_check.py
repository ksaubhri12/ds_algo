class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def is_binary_tree_heap_check(root: Node):
    if root is None:
        return [float('-inf'), True]

    if root.left is None and root.right is not None:
        return [root.data, False]

    left_node_value_and_check = is_binary_tree_heap_check(root.left)
    right_node_value_and_check = is_binary_tree_heap_check(root.right)
    left_node_value = left_node_value_and_check[0]
    left_check = left_node_value_and_check[1]
    right_node_value = right_node_value_and_check[0]
    right_check = right_node_value_and_check[1]

    final_check = left_check and right_check and root.data > left_node_value and root.data > right_node_value
    return [root.data, final_check]


def check_completeness(root: Node):
    final_arr = []
    data_queue = [root]
    while len(data_queue) > 0:
        size = len(data_queue)
        for i in range(size):
            element_pop = data_queue.pop(0)

            if element_pop is None:
                final_arr.append(None)
                continue
            final_arr.append(element_pop.data)
            data_queue.append(element_pop.left)
            data_queue.append(element_pop.right)

    n = len(final_arr)
    none_index = -1
    element_index = -1
    for i in range(n):
        if none_index < element_index and none_index != -1:
            return False

        if final_arr[i] is None:
            none_index = i
        else:
            element_index = i

    return True


def check_binary_tree_heap(root: Node):
    if is_binary_tree_heap_check(root)[1]:
        return check_completeness(root)
    else:
        return False


if __name__ == '__main__':
    anode_1 = Node(5)
    anode_2 = Node(2)
    anode_3 = Node(3)

    anode_1.left = anode_2
    anode_1.right = anode_3
    # print(check_binary_tree_heap(anode_1))

    node_1 = Node(40)
    node_2 = Node(10)
    node_3 = Node(30)
    node_1.left = node_2
    node_1.right = node_3

    node_4 = Node(15)
    node_5 = Node(25)

    node_3.left = node_4
    node_3.right = node_5
    print(check_binary_tree_heap(node_1))

