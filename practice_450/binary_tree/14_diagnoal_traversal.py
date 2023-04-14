# In diagonally you have to add all the right node and you have to address all the left node later.
# so traverse all the right node and add them in the answer. However for the left node just add them into a queue and
# after that traverse the queue and do the same for remaining nodes.
# for starter add the root into the queue by yourself.

from Node import Node


def diagonal_traversal(root: Node):
    traverse_queue = [root]
    final_result = []

    while len(traverse_queue) > 0:
        node_pop = traverse_queue.pop(0)
        final_result.append(node_pop.data)
        curr = node_pop
        while curr is not None:
            if curr.left is not None:
                traverse_queue.append(curr.left)
            curr = curr.right
            if curr is not None:
                final_result.append(curr.data)

    return final_result


if __name__ == '__main__':
    node_1 = Node(1)
    node_2 = Node(39)
    node_3 = Node(10)
    node_4 = Node(5)

    node_1.left = node_2
    node_1.right = node_3
    node_2.left = node_4

    print(diagonal_traversal(node_1))
