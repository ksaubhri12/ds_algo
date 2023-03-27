from Node import Node
from LinkedList import LinkedList


def seggregate_even_odd(head: Node):
    even = None
    odd = None
    e = None
    o = None

    while head is not None:
        data = head.data
        if data % 2 == 0:
            if even is None:
                even = head
                e = head

            else:
                e.next = head
                e = e.next

        else:
            if odd is None:
                odd = head
                o = head
            else:
                o.next = head
                o = o.next

        head = head.next

    if e is not None:
        e.next = odd
    if o is not None:
        o.next = None

    if even is not None:
        return even
    else:
        return odd


if __name__ == '__main__':
    node_1 = Node(12)
    node_2 = Node(15)
    node_3 = Node(10)
    node_4 = Node(11)
    node_5 = Node(5)
    node_6 = Node(6)
    node_7 = Node(2)
    node_8 = Node(3)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6
    node_6.next = node_7
    node_7.next = node_8

    print('Current Linked List')
    LinkedList(node_1).print_linked_list()
    print('Segregating and printing')
    new_head_node = seggregate_even_odd(node_1)
    LinkedList(new_head_node).print_linked_list()
