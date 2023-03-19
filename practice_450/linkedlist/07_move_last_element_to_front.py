from Node import Node
from LinkedList import LinkedList


def move_last_element_front(head: Node):
    curr = head
    prev = None
    while curr.next is not None:
        prev = curr
        curr = curr.next
    prev.next = None
    curr.next = head
    return curr


if __name__ == '__main__':
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    print('Current Linked List')
    ll = LinkedList(node_1)
    ll.print_linked_list()
    print('Remove Duplicate')
    head = move_last_element_front(node_1)
    ll = LinkedList(head)
    ll.print_linked_list()
