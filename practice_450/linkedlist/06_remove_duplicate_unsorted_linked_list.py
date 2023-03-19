from Node import Node
from LinkedList import LinkedList


def remove_duplicate_in_linked_list(head: Node):
    value_dict = {}
    curr = head
    prev = None
    while curr is not None:
        if curr.data in value_dict:
            temp = curr.next
            prev.next = temp
            curr = temp
        else:
            value_dict[curr.data] = 1
            prev = curr
            curr = curr.next

    return head


if __name__ == '__main__':
    node_1 = Node(2)
    node_2 = Node(3)
    node_3 = Node(4)
    node_4 = Node(3)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    print('Current Linked List')
    ll = LinkedList(node_1)
    ll.print_linked_list()
    print('Remove Duplicate')
    head = remove_duplicate_in_linked_list(node_1)
    ll = LinkedList(head)
    ll.print_linked_list()
