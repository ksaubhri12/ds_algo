from Node import Node


def intersection_point(head_1: Node, head_2: Node):
    count_head_1 = get_count(head_1)
    count_head_2 = get_count(head_2)
    if count_head_1 > count_head_2:
        dist = count_head_1 - count_head_2
        node_tra = head_1
        second_node = head_2

    else:
        dist = count_head_2 - count_head_1
        node_tra = head_2
        second_node = head_1

    while dist > 0:
        dist = dist - 1
        node_tra = node_tra.next

    while node_tra is not None and second_node is not None:
        if node_tra.next == second_node.next and node_tra.next is not None:
            return node_tra.next.data
        node_tra = node_tra.next
        second_node = second_node.next

    return -1


def get_count(head: Node):
    count = 0
    curr = head
    while curr is not None:
        count = count + 1
        curr = curr.next

    return count


if __name__ == '__main__':
    node_1 = Node(3)
    node_2 = Node(6)
    node_3 = Node(9)
    node_4 = Node(15)
    node_5 = Node(30)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5

    mnode_1 = Node(10)
    mnode_1.next = node_4

    print(intersection_point(node_1, mnode_1))