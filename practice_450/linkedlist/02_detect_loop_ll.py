class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def detect_loop(head):
    slow = head
    fast = head.next.next
    answer = False
    while slow is not None and fast is not None and fast.next is not None:
        if slow == fast:
            answer = True
            break
        slow = slow.next
        fast = fast.next.next

    return answer


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(3)
    next_node = Node(3)
    head.next.next = next_node
    next_node.next = Node(4)
    loop_node = next_node.next
    next_node.next.next = Node(5)
    next_node.next.next.next = Node(6)
    next_node.next.next.next.next = loop_node
    print(detect_loop(head))


