from Node import Node


def check_circular_linked_list(head: Node):
    if head is None:
        return True

    curr = head
    answer = False
    while curr is not None:
        curr = curr.next
        if curr == head:
            answer = True
            break

    return answer

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
    print(check_circular_linked_list(node_1))
    node_6.next = node_1
    print(check_circular_linked_list(node_1))
