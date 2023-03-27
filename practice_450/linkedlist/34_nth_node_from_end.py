from Node import Node


def nth_node_from_end(head: Node, n: int):
    total_count = get_count(head)
    k = n - total_count + 1
    get_from_start(head, k)


def get_from_start(head: Node, k: int):
    count = 1
    curr = head
    while count < k:
        count = count + 1
        curr = curr.next

    return curr


def get_count(head: Node):
    count = 0
    curr = head
    while curr is not None:
        count = count + 1
        curr = curr.next

    return count
