from Node import Node
from LinkedList import LinkedList


def delete_nodes_greater_val_right_side(head: Node):
    new_head = reverse_linked_list(head)
    max_value = new_head.data
    curr = new_head
    prev = None
    while curr is not None:
        if curr.data < max_value:
            prev.next = curr.next
            curr = curr.next
            continue

        if curr is not None and curr.data > max_value:
            max_value = curr.data

        prev = curr
        curr = curr.next

    return reverse_linked_list(new_head)


def reverse_linked_list(head: Node):
    curr = head
    prev = None

    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


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
    print('Delete Elements')
    new_head_v2 = delete_nodes_greater_val_right_side(node_1)
    LinkedList(new_head_v2).print_linked_list()
