from Node import Node
from LinkedList import LinkedList


def deletion_node(head: Node, key):
    curr = head
    prev = None
    while curr.data != key:
        prev = curr
        curr = curr.next

    curr_next = curr.next
    prev.next = curr_next
    curr = None
    return head


def reverse_circular_linked_list(head: Node):
    curr = head.next
    prev = head
    while curr != head:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    head.next = prev
    return prev


if __name__ == '__main__':
    node_1 = Node(10)
    node_2 = Node(7)
    node_3 = Node(8)
    node_4 = Node(4)
    node_5 = Node(6)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_1

    head = deletion_node(node_1, 8)
    node = reverse_circular_linked_list(head)
    ll = LinkedList(node)
    ll.print_circular_linked_list()
