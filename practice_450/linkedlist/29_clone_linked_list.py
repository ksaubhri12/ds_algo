from LinkedList import LinkedList


class SpecialNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.arb = None


def clone_linked_list(head: SpecialNode):
    curr = head
    while curr is not None:
        temp_next_node = curr.next
        data = curr.data
        new_node = SpecialNode(data)
        curr.next = new_node
        new_node.next = temp_next_node
        curr = temp_next_node

    curr = head
    while curr is not None:
        if curr.arb is not None:
            curr.next.arb = curr.arb.next

        curr = curr.next.next

    original = head
    copy = head.next
    temp = copy
    while original is not None and copy is not None:
        original.next = original.next.next
        if copy.next is not None:
            copy.next = copy.next.next
        original = original.next
        copy = copy.next

    return temp


if __name__ == '__main__':
    node_1 = SpecialNode(12)
    node_2 = SpecialNode(15)
    node_3 = SpecialNode(10)
    node_4 = SpecialNode(11)
    node_5 = SpecialNode(5)
    node_6 = SpecialNode(6)
    node_7 = SpecialNode(2)
    node_8 = SpecialNode(3)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6
    node_6.next = node_7
    node_7.next = node_8

    clone_linked_list(node_1)
    LinkedList(node_1).print_linked_list()
