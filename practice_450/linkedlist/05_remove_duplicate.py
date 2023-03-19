from Node import Node
from LinkedList import LinkedList

def remove_duplicate(head: Node):
    curr = head
    prev = None
    while curr is not None:
        if prev is not None and prev.data == curr.data:
            temp = curr.next
            prev.next = temp
            curr = None
            curr = temp
        else:
            temp = curr.next
            prev = curr
            curr = temp

    return head


if __name__ == '__main__':
    node_1 = Node(1)
    node_2 = Node(3)
    node_3 = Node(3)
    node_4 = Node(4)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    print('Current Linked List')
    ll = LinkedList(node_1)
    ll.print_linked_list()
    print('Sort the Linked List')
    head = remove_duplicate(node_1)
    ll = LinkedList(head)
    ll.print_linked_list()
