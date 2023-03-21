from Node import Node


def get_middle_element(head: Node):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


if __name__ == '__main__':
    node_1 = Node(3)
    node_2 = Node(6)
    node_3 = Node(9)
    node_4 = Node(15)
    node_5 = Node(30)
    node_6 = Node(40)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6

    node = get_middle_element(node_1)
    print(node.data)
