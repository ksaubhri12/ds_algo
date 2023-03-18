class Node:
    def __init__(self, value: int, next_node):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self, head: Node):
        self.head = head

    def print_linked_list(self):
        curr = self.head
        while curr is not None:
            print(curr.value, end = ' ')
            curr = curr.next_node
        print()


def reverse_linked_list_group_k(head: Node, k):
    if head is None:
        return
    if head.next_node is None:
        return head
    last_node_prev_node = reverse_util(head, k)
    last_node = last_node_prev_node[0]
    head.next_node = reverse_linked_list_group_k(last_node, k)
    return last_node_prev_node[1]


def reverse_util(head: Node, k: int):
    count = 0
    curr = head
    prev = None
    while curr is not None and count < k:
        temp = curr.next_node
        curr.next_node = prev
        count = count + 1
        prev = curr
        curr = temp

    return [curr, prev]


if __name__ == '__main__':
    node_1 = Node(1, Node(2, Node(2, Node(4, Node(5, Node(6, Node(7, Node(8, None))))))))
    ll = LinkedList(node_1)
    print('curr linked list')
    ll.print_linked_list()
    print('reversing it')
    new_head = reverse_linked_list_group_k(node_1, 4)
    print('new linked list after reversing it')
    ll = LinkedList(new_head)
    ll.print_linked_list()
