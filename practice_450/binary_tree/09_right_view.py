# This is also a level order traversal but here first add the right child into queue and then left for next level
# iteration. After that print the first element.

from Node import Node


def right_view(root: Node):
    if root is None:
        return []

    answer = []
    traverse_queue = [root]
    while len(traverse_queue) > 0:
        queue_size = len(traverse_queue)
        element = traverse_queue[0]
        answer.append(element.data)
        for i in range(0, queue_size):
            traverse_node = traverse_queue.pop(0)
            if traverse_node.right is not None:
                traverse_queue.append(traverse_node.right)
            if traverse_node.left is not None:
                traverse_queue.append(traverse_node.left)

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

    print(right_view(node_1))
