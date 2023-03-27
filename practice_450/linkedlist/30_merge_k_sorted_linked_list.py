from Node import Node
from LinkedList import LinkedList


def merge_k_sorted_linked_list(arr: [Node], k: int):
    i = 0
    last = k - 1
    while last != 0:
        i = 0
        j = last
        while i < j:
            arr[i] = merge_two_sorted_linked_list(arr[i], arr[j])
            i = i + 1
            j = j - 1
            if i >= j:
                last = j

    return arr[0]


def merge_two_sorted_linked_list(head_1: Node, head_2: Node):
    if head_1 is None:
        return head_2
    if head_2 is None:
        return head_1

    result = None
    if head_1.data <= head_2.data:
        result = head_1
        result.next = merge_two_sorted_linked_list(head_1.next, head_2)

    else:
        result = head_2
        result.next = merge_two_sorted_linked_list(head_1, head_2.next)

    return result


if __name__ == '__main__':
    node_1 = Node(1)
    node_2 = Node(4)
    node_3 = Node(5)

    node_1.next = node_2
    node_2.next = node_3

    anode_1 = Node(3)
    anode_2 = Node(7)
    anode_3 = Node(8)

    anode_1.next = anode_2
    anode_2.next = anode_3

    bnode_1 = Node(10)
    bnode_2 = Node(11)
    bnode_3 = Node(12)

    bnode_1.next = bnode_2
    bnode_2.next = bnode_3

    new_head = merge_k_sorted_linked_list([node_1, anode_1, bnode_1], 3)
    LinkedList(new_head).print_linked_list()
