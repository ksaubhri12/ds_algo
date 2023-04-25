class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, node: Node):
        self.head = node

    def print(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=' ')
            curr = curr.next

        print()


def remove_k_from_last(head: Node, k: int):
    if head is None:
        return None
    slow = head
    prev = None
    fast = head
    c = 0
    for i in range(k):
        c = c + 1
        if fast is not None:
            fast = fast.next
        else:
            break

    last_head_check = k - c == 0

    if fast is None and not last_head_check:
        return head
    if fast is None:
        res = head.next
        head.data = None
        head.next = None
        return res

    while fast is not None:
        prev = slow
        slow = slow.next
        fast = fast.next

    prev.next = slow.next
    slow.next = None
    slow.data = None

    return head


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    print('Current Linked List')

    LinkedList(node_1).print()
    print('Remove 5th element')
    new_head = remove_k_from_last(node_1, 5)
    # new_head = remove_k_from_last(node_1, 3)
    LinkedList(new_head).print()
