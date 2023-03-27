class SpecialNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.bottom = None


class SpecialLinkedList:
    def __init__(self, head: SpecialNode):
        self.head = head

    def print_sll(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=' ')
            curr = curr.bottom

        print()


def flatten_linked_list(head: SpecialNode):
    curr = head
    new_head = head
    while curr is not None:
        next_list = curr.next
        new_head = merge_two_sorted_special_linked_list(new_head, next_list)
        curr.next = None
        curr = next_list

    return new_head


def merge_two_sorted_special_linked_list(head_1: SpecialNode, head_2: SpecialNode):
    if head_1 is None:
        return head_2
    if head_2 is None:
        return head_1
    new_merge_head = head_1
    curr = head_2
    while curr is not None:
        next_to_pick = curr.bottom
        curr.bottom = None
        new_merge_head = insert_element_in_sorted_linked_list(new_merge_head, curr)
        curr = next_to_pick
    return new_merge_head


def insert_element_in_sorted_linked_list(head_1: SpecialNode, element: SpecialNode):
    if element.data < head_1.data:
        element.bottom = head_1
        return element

    prev = head_1
    curr = head_1.bottom
    insertion_done = False
    while curr is not None:
        if prev.data == element.data or curr.data == element.data:
            prev.bottom = element
            element.bottom = curr
            insertion_done = True
            break
        if prev.data < element.data < curr.data:
            prev.bottom = element
            element.bottom = curr
            insertion_done = True
            break
        prev = curr
        curr = curr.bottom

    if prev.data < element.data and not insertion_done:
        prev.bottom = element

    return head_1


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

    node_2.next = node_3
    node_2.bottom = node_2_1
    node_2_1.bottom = None

    node_3.next = node_4
    node_3.bottom = node_3_1
    node_3_1.bottom = node_3_2

    node_4.next = None
    node_4.bottom = node_4_1
    node_4_1.bottom = node_4_2
    node_4_2.bottom = node_4_3

    print('Current Linked List')
    SpecialLinkedList(node_1).print_sll()
    print('Flatten')

    new_node = flatten_linked_list(node_1)
    SpecialLinkedList(new_node).print_sll()

