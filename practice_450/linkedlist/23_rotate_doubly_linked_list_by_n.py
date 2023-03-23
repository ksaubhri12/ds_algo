from Node import Node
from LinkedList import LinkedList


def rotate_doubly_linked_list_by_n(head: Node, k: int):
    curr = head
    while curr.next is not None:
        curr = curr.next
    end = curr
    return rotate_linked_list_by_n(head, end, k)


def rotate_linked_list_by_n(start: Node, end: Node, k: int):
    if k == 0:
        return start

    new_head = start.next
    end.next = start
    start.next = None
    new_head.prev = None
    return rotate_linked_list_by_n(new_head, start, k - 1)

if __name__ == '__main__':
    node_1 = Node(6)
    node_2 = Node(5)
    node_3 = Node(3)
    node_4 = Node(2)
    node_5 = Node(8)
    node_6 = Node(10)
    node_7 = Node(9)
    node_8 = Node(-1)

    node_1.next = node_2
    node_2.next = node_3
    node_2.prev = node_1

    node_3.next = node_4
    node_3.prev = node_2

    node_4.next = node_5
    node_4.prev = node_3

    node_5.next = node_6
    node_5.prev = node_4

    node_6.next = node_7
    node_6.prev = node_5

    node_7.next = node_8
    node_7.prev = node_6

    node_8.prev = node_7

    print('Current Linked List')
    LinkedList(node_1).print_linked_list()
    print('Rotate Current Linked List by 2')
    new_node = rotate_doubly_linked_list_by_n(node_1, 2)
    LinkedList(new_node).print_linked_list()
