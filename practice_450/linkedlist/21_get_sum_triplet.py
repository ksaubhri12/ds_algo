from Node import Node


def count_triplet(head: Node, k):
    start = head
    curr = head
    while curr.next is not None:
        curr = curr.next

    end_node = curr

    count = 0
    while start is not None and start.next is not None and start.next.next is not None:
        first_value = start
        remaining_sum = k - first_value.data
        second = start.next
        end = end_node
        while second.data < end.data:
            sum_value = second.data + end.data
            if sum_value == remaining_sum:
                count = count + 1
                second = second.next
                end = end.prev

            elif sum_value < remaining_sum:
                second = second.next

            else:
                end = end.prev
        start = start.next

    return count


if __name__ == '__main__':
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(4)
    node_4 = Node(5)
    node_5 = Node(6)
    node_6 = Node(8)
    node_7 = Node(9)

    node_1.next = node_2
    node_2.next = node_3
    node_2.prev = node_1

    node_3.next = node_4
    node_3.prev = node_2

    node_4.next = node_5
    node_4.prev = node_3

    node_5.next = node_6
    node_5.prev = node_4

    node_6.next = node_7
    node_6.prev = node_5

    node_7.prev = node_6

    print(count_triplet(node_1, 15))
