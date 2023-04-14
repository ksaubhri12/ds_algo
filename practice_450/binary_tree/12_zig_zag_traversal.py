# At every level traversal maintain a variable as normal which will tell in the final answer
# we will stack element of that level in straight order or reverse order.
# if you do straight make normal as false
# if you do reverse make normal as true

from Node import Node


def zig_zag_traversal(root: Node):
    answer = []
    if root is None:
        return answer

    traverse_queue = []
    traverse_queue.append(root)
    normal = True
    while len(traverse_queue) > 0:
        queue_size = len(traverse_queue)
        if normal:
            answer.extend(traverse_queue[0:queue_size])
            normal = False
        else:
            normal = True
            answer.extend(reversed(traverse_queue[0:queue_size]))

        for i in range(0, queue_size):
            traverse_node = traverse_queue.pop(0)
            if traverse_node.left is not None:
                traverse_queue.append(traverse_node.left)
            if traverse_node.right is not None:
                traverse_queue.append(traverse_node.right)

    answer_val = []
    for obj in answer:
        answer_val.append(obj.data)

    return answer_val


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
    print(zig_zag_traversal(node_1))
