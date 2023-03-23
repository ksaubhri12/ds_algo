class SpecialNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.bottom = None


def flatten_linked_list(head: SpecialNode):
    curr = head
    while curr is not None:
        next_node = curr.next
        curr_node = curr
        while curr_node.bottom is not None:
            curr_node.next = curr_node.bottom
            curr_node = curr_node.bottom

        curr_node.next = next_node

    return head


if __name__ == '__main__':
    node_1 = SpecialNode(5)
    node_1_2 = SpecialNode(7)
    node_1_3 = SpecialNode(8)
    node_1_4 = SpecialNode(30)

    node_2 = SpecialNode(10)
    node_2_1 = SpecialNode(20)

    node_3 = SpecialNode(19)
    node_3_1 = SpecialNode(22)
    node_3_2 = SpecialNode(50)

    node_4 = SpecialNode(28)
    node_4_1 = SpecialNode(35)
    node_4_2 = SpecialNode(40)
    node_4_3 = SpecialNode(45)

    node_1.next = node_2
    node_1.bottom = node_1_2
    node_1_2.bottom = node_1_3
    node_1_3.bottom = node_1_4

    # node_2.next =

