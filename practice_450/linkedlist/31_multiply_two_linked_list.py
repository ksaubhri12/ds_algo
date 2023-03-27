from Node import Node


def multiply_two_linked_list(head_1: Node, head_2: Node):
    final_string = ''
    curr = head_1
    while curr is not None:
        final_string = final_string + str(curr.data)
        curr = curr.next

    int_1 = int(final_string)

    final_string = ''
    curr = head_2
    while curr is not None:
        final_string = final_string + str(curr.data)
        curr = curr.next
    int_2 = int(final_string)

    return int_1 * int_2
