from Node import Node
from LinkedList import LinkedList


def intersection_linked_list(head_1: Node, head_2: Node):
    dict_1 = {}
    dict_2 = {}

    dict_1 = set_dict_from_linked_list(head_1, dict_1)
    dict_2 = set_dict_from_linked_list(head_2, dict_2)

    new_head = None
    curr = new_head
    for key in dict_1.keys():
        count_occurrence = dict_1[key]
        if key in dict_2:
            count_occurrence_2 = dict_2[key]
            final_count = min(count_occurrence, count_occurrence_2)
            if new_head is None:
                new_head = Node(key)
                curr = new_head
                for i in range(0, final_count - 1):
                    curr.next = Node(key)
                    curr = curr.next
            else:
                for i in range(0, final_count):
                    curr.next = Node(key)
                    curr = curr.next

    return new_head


def set_dict_from_linked_list(head: Node, dict_value: {}):
    curr = head
    while curr is not None:
        data = curr.data
        curr = curr.next
        if data in dict_value:
            dict_value[data] = dict_value[data] + 1
        else:
            dict_value[data] = 1

    keys = list(dict_value.keys())
    keys.sort()
    sorted_dict = {i: dict_value[i] for i in keys}
    dict_value = sorted_dict
    return dict_value


if __name__ == '__main__':
    node_1 = Node(4)
    node_2 = Node(8)
    node_3 = Node(15)
    node_4 = Node(17)
    node_5 = Node(18)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5

    mnode_1 = Node(4)
    mnode_2 = Node(10)
    mnode_3 = Node(18)
    mnode_1.next = mnode_2
    mnode_2.next = mnode_3


    new_head = intersection_linked_list(node_1, mnode_1)
    ll = LinkedList(new_head)
    ll.print_linked_list()
