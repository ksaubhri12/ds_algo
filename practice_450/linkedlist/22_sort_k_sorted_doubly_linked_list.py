from queue import PriorityQueue
from Node import Node
from LinkedList import LinkedList


def sort_k_sorted_doubly_linked_list(head: Node, k: int):
    pq = PriorityQueue()
    curr = head
    count = 0
    while curr is not None and count <= k:
        pq.put((curr.data, curr))
        count = count + 1
        curr = curr.next

    new_head = None
    cur = None
    while not pq.empty():
        if new_head is None:
            new_head = pq.get()[1]
            new_head.prev = None
            cur = new_head

        else:
            pop_element = pq.get()[1]
            cur.next = pop_element
            pop_element.prev = cur
            cur = pop_element

        if curr is not None:
            pq.put((curr.data, curr))
            curr = curr.next

    cur.next = None

    return new_head


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
    print('Sorting the linked list')
    new_node = sort_k_sorted_doubly_linked_list(node_1, 4)
    LinkedList(new_node).print_linked_list()
