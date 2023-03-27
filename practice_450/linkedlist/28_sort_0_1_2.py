from Node import Node
from LinkedList import LinkedList


def sort_0_1_2(head: Node):
    zero_count = 0
    one_count = 0
    two_count = 0

    curr = head
    while curr is not None:
        value = curr.data
        if value == 0:
            zero_count = zero_count + 1
        elif value == 1:
            one_count = one_count + 1
        else:
            two_count = two_count + 1
        curr = curr.next

    new_head = None
    curr = None
    while zero_count > 0 or one_count > 0 or two_count > 0:
        if zero_count > 0:
            if new_head is None:
                new_head = Node(0)
                curr = new_head

            else:
                curr.next = Node(0)
                curr = curr.next

            zero_count = zero_count - 1

        elif one_count > 0:
            if new_head is None:
                new_head = Node(1)
                curr = new_head

            else:
                curr.next = Node(1)
                curr = curr.next

            one_count = one_count - 1

        elif two_count > 0:

            if new_head is None:
                new_head = Node(2)
                curr = new_head

            else:
                curr.next = Node(2)
                curr = curr.next

            two_count = two_count - 1

    return new_head


if __name__ == '__main__':
    node_1 = Node(0)
    node_2 = Node(1)
    node_3 = Node(2)
    node_4 = Node(0)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4

    print('Current Linked List')
    LinkedList(node_1).print_linked_list()
    print('Perform Sorting')
    new_head_node = sort_0_1_2(node_1)
    print('Sorted Linked List')
    LinkedList(new_head_node).print_linked_list()
