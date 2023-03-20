import math

from Node import Node
from LinkedList import LinkedList


def add_two_numbers(head_1: Node, head_2: Node):
    number_1 = get_number_from_linked_list(head_1)
    number_2 = get_number_from_linked_list(head_2)
    final_sum = number_1 + number_2
    number_len = len(str(final_sum))
    new_head = None
    curr = new_head
    value = str(final_sum)
    for i in range(0, number_len):
        char = int(value[i])
        if new_head is None:
            new_head = Node(char)
            curr = new_head
        else:
            curr.next = Node(char)
            curr = curr.next

    return new_head



def get_number_from_linked_list(head: Node):
    final_string = ''
    curr = head
    while curr is not None:
        final_string = final_string + str(curr.data)
        curr = curr.next

    return int(final_string)


if __name__ == '__main__':
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4

    mnode_1 = Node(1)
    mnode_2 = Node(2)
    mnode_3 = Node(3)
    mnode_4 = Node(4)
    mnode_1.next = mnode_2
    mnode_2.next = mnode_3
    mnode_3.next = mnode_4

    new_head = add_two_numbers(node_1, mnode_1)
    ll = LinkedList(new_head)
    ll.print_linked_list()
