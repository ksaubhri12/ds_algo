def print_linked_list(head):
    curr = head
    while curr is not None:
        print(curr.value)
        curr = curr.next_node


class LinkedList:
    def __init__(self, value: int, next_node):
        self.value = value
        self.next_node = next_node


def reverse_linked_list(head: LinkedList):
    curr = head
    prev = None
    while curr is not None:
        temp = curr.next_node
        curr.next_node = prev
        prev = curr
        curr = temp
    return prev


if __name__ == '__main__':
    node_1 = LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4, LinkedList(5, None)))))
    print_linked_list(node_1)
    new_head = reverse_linked_list(node_1)
    print_linked_list(new_head)
