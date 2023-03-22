from Node import Node
from LinkedList import LinkedList


def reverse_doubly_linked_list(head: Node):
    curr = head
    prev_node = None
    while curr is not None:
        temp = curr.next
        curr.next = prev_node
        curr.prev = temp
        prev_node = curr
        curr = temp

    return prev_node


if __name__ == '__main__':
    node_1 = Node(3)
    node_2 = Node(4)
    node_3 = Node(5)
    node_1.next = node_2
    node_2.next = node_3
    node_2.prev = node_1
    node_3.prev = node_2

    print('Current Linked List')
    LinkedList(node_1).print_linked_list()
    print('Reversed the Linked List')
    new_head = reverse_doubly_linked_list(node_1)
    LinkedList(new_head).print_linked_list()
