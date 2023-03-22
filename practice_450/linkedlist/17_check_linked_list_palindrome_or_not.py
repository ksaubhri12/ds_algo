from Node import Node


def check_list_palindrome_or_not(head: Node):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    prev = None
    curr = slow
    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    answer = True
    first_end = head
    last_end = prev
    while first_end is not None and last_end is not None:
        if first_end.data != last_end.data:
            answer = False
            break
        else:
            first_end = first_end.next
            last_end = last_end.next

    return answer


if __name__ == '__main__':
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(3)
    node_6 = Node(2)
    node_7 = Node(9)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6
    node_6.next = node_7

    print(check_list_palindrome_or_not(node_1))
