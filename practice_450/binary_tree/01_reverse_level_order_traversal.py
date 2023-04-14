# The idea is to append root in the last. Normal append function will add the last element in the last.
# That is why we have used deque -> A deque is a double ended queue where you can add element in the front and
# in the back
# We keep on adding element in front for deque
# The queue for level -> We will add the right element first and then the left element
# we will pop only one element from queue and append in front of answer deque using append_left function.

from Node import Node
from collections import deque


def reverse_level_order_traversal(root: Node):
    if root is None:
        return None
    answer = deque()
    q = deque()
    q.append(root)
    while q:
        result_node = q.popleft()
        if result_node is None:
            continue

        answer.appendleft(result_node.data)

        if result_node.right is not None:
            q.append(result_node.right)

        if result_node.left is not None:
            q.append(result_node.left)

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

    print(list(reverse_level_order_traversal(node_1)))
