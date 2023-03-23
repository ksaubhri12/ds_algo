from Node import Node
from LinkedList import LinkedList


def reverse_doubly_linked_list(head: Node, k: int):
    if head is None or head.next is None:
        return head

    curr_prev = reverse_in_group_k(head, k)
    head.next = reverse_doubly_linked_list(curr_prev[0], k)
    return curr_prev[1]


def reverse_in_group_k(head: Node, k: int):
    count = 0
    curr = head
    prev = None
    while curr is not None and count < k:
        temp = curr.next
        curr.next = prev
        curr.prev = temp
        prev = curr
        curr = temp
        count = count + 1

    prev.prev = None
    return [curr, prev]


if __name__ == '__main__':
    node_1 = Node(6)
    node_2 = Node(5)
    node_3 = Node(3)
    node_4 = Node(2)
    node_5 = Node(8)
    node_6 = Node(10)
    node_7 = Node(9)

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

    node_7.prev = node_6

    print('Current Linked List')
    LinkedList(node_1).print_linked_list()

    print('Reverse Linked List in group of 3')
    new_head_node = reverse_doubly_linked_list(node_1, 3)
    LinkedList(new_head_node).print_linked_list()
