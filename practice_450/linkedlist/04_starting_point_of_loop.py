from Node import Node


def starting_point_of_loop(head: Node):
    if head.next is None:
        return head

    slow = head.next
    fast = head.next.next
    answer = False
    while slow is not None and fast is not None and fast.next is not None:
        if slow == fast:
            answer = True
            break
        else:
            slow = slow.next
            fast = fast.next.next

    if answer is not True:
        return None

    if slow == head and fast == head:
        return head
    else:
        slow = head
        while True:
            if slow.next == fast.next:
                return slow.next
            else:
                slow = slow.next
                fast = fast.next


if __name__ == '__main__':
    node_1 = Node(1)
    node_2 = Node(3)
    node_3 = Node(4)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_2
    node = starting_point_of_loop(node_1)

    print(node.data)
