class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head: Node):
        self.head = head

    def print_linked_list(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=' ')
            curr = curr.next
        print()


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

    fast.next.next = None
    return head


if __name__ == '__main__':
    node_1 = Node(1)
    node_2 = Node(3)
    node_3 = Node(4)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_2
    head = detect_loop(node_1)
    ll = LinkedList(head)
    ll.print_linked_list()






    head = Node(1)
    head.next = Node(3)
    next_node = Node(3)
    head.next.next = next_node
    next_node.next = Node(4)
    loop_node = next_node.next
    next_node.next.next = Node(5)
    next_node.next.next.next = Node(6)
    next_node.next.next.next.next = loop_node
    head = detect_loop(head)
    ll = LinkedList(head)
    ll.print_linked_list()
