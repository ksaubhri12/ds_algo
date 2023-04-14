# Here basically do a level order traversal and at each level, print the first element in the result stack.

from Node import Node


def left_view(root: Node):
    if root is None:
        return []

    answer = []
    traverse_queue = []
    traverse_queue.append(root)
    while len(traverse_queue) > 0:
        queue_size = len(traverse_queue)
        front_element = traverse_queue[0]
        answer.append(front_element.data)
        for i in range(0, queue_size):
            level_node = traverse_queue.pop(0)
            if level_node.left is not None:
                traverse_queue.append(level_node.left)
            if level_node.right is not None:
                traverse_queue.append(level_node.right)

    return answer


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

    print(left_view(node_1))
