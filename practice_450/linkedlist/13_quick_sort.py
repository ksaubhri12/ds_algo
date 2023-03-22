from Node import Node
from LinkedList import LinkedList

def partition(arr: [], start: int, end: int):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] < pivot:
            i = i + 1
            arr[j], arr[i] = arr[i], arr[j]

    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


def quick_sort(arr: [], start: int, end: int):
    if start < end:
        part = partition(arr, start, end)
        quick_sort(arr, start, part - 1)
        quick_sort(arr, part + 1, end)

    return arr


def quick_sort_linked_list(head: Node):
    curr = head
    while curr.next is not None:
        curr = curr.next

    quicksort_linked_list_util(head, curr)


def partition_linked_list(start: Node, end: Node):
    if start == end or start is None or end is None:
        return start
    pivot_prev = start
    curr = start
    pivot = end.data

    while start != end:
        if start.data < pivot:
            pivot_prev = curr
            temp = curr.data
            curr.data = start.data
            start.data = temp
            curr = curr.next

        start = start.next

    temp = curr.data
    curr.data = pivot
    end.data = temp

    return pivot_prev


def quicksort_linked_list_util(start: Node, end: Node):
    if start is None or start == end or start.next == end:
        return
    pivot_prev = partition_linked_list(start, end)
    quicksort_linked_list_util(start, pivot_prev)

    if pivot_prev is not None and pivot_prev == start:
        quicksort_linked_list_util(pivot_prev.next, end)

    elif pivot_prev is not None and pivot_prev.next is not None:
        quicksort_linked_list_util(pivot_prev.next.next, end)


def partition_v2(arr: [], start, end):
    pivot = arr[start]
    i = end
    for j in reversed(range(start + 1, end + 1)):
        if arr[j] > pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i = i - 1

    arr[i], arr[start] = arr[start], arr[i]
    return i - 1


if __name__ == '__main__':
    node_1 = Node(10)
    node_2 = Node(6)
    node_3 = Node(9)
    node_4 = Node(11)
    node_5 = Node(2)
    node_6 = Node(4)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6

    ll_1 = LinkedList(node_1)
    print('Current Linked List')
    ll_1.print_linked_list()
    print('Perform Sorting Operation')
    quick_sort_linked_list(node_1)
    ll_1 = LinkedList(node_1)
    ll_1.print_linked_list()

