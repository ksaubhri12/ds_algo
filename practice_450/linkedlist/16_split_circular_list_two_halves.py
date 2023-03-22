from Node import Node


def split_circular_list_two_halves(head: Node, head_1: Node, head_2: Node):
    if head is None:
        head_1 = None
        head_2 = None

    if head.next is None:
        head_1 = head
        head_2 = head

    count = 1
    curr = head.next
    while curr != head:
        count = count + 1
        curr = curr.next

    head_1 = head
    k = 0
    curr = head
    if count % 2 == 0:
        traverse = count // 2 - 1
    else:
        traverse = count // 2

    while k < traverse:
        curr = curr.next
        k = k + 1

    head_2 = curr

    return head_1, head_2


if __name__ == '__main__':
    node_1 = Node(3)
    node_2 = Node(6)
    node_3 = Node(9)
    node_4 = Node(15)
    node_5 = Node(30)
    node_6 = Node(40)
    node_7 = Node(1)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6
    node_6.next = node_7
    node_7.next = node_1
    # head_1, head_2 = (split_circular_list_two_halves(node_1, None, None))
    # print(head_1.data, head_2.data)

    anode_1 = Node(1)
    anode_2 = Node(5)
    anode_3 = Node(7)
    anode_1.next = anode_2
    anode_2.next = anode_3
    anode_3.next = anode_1
    head_1, head_2 = (split_circular_list_two_halves(anode_1, None, None))
    print(head_1.data, head_2.data)

