from queue import PriorityQueue


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head: Node):
        self.head = head

    def print(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=' ')
            curr = curr.next

        print()


def merge_k_sorted_linked_list(input_arr: [Node], k):
    final_head = None
    curr = None
    data_queue = PriorityQueue()
    for i in range(k):
        head = input_arr[i]
        data_queue.put((head.data, i, head))

    while len(data_queue.queue) > 0:
        element_data = data_queue.get()
        element_popped = element_data[2]
        if final_head is None:
            final_head = element_popped
            curr = element_popped

        else:
            temp = curr
            temp.next = element_popped
            curr = element_popped

        if element_popped.next is not None:
            next_element = element_popped.next
            list_number = element_data[1]
            data_queue.put((next_element.data, list_number, next_element))

    return final_head


if __name__ == '__main__':
    node_1 = Node(1)
    node_2 = Node(4)
    node_3 = Node(5)

    node_1.next = node_2
    node_2.next = node_3

    anode_1 = Node(3)
    anode_2 = Node(7)
    anode_3 = Node(8)

    anode_1.next = anode_2
    anode_2.next = anode_3

    bnode_1 = Node(10)
    bnode_2 = Node(11)
    bnode_3 = Node(12)

    bnode_1.next = bnode_2
    bnode_2.next = bnode_3

    new_head = merge_k_sorted_linked_list([node_1, anode_1, bnode_1], 3)

    LinkedList(new_head).print()
