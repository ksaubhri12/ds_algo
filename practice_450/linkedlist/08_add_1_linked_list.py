import math

from Node import Node
from LinkedList import LinkedList


def add_1_linked_list(head: Node):
    final_string = ''
    curr = head
    while curr is not  None:
        final_string = final_string + str(curr.data)
        curr = curr.next

    int_number = int(final_string)
    return Node(int_number+1)


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
    print('Doing add 1 operation')
    head = add_1_linked_list(node_1)
    ll = LinkedList(head)
    ll.print_linked_list()
