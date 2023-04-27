def merge_two_binary_heaps(heap_arr1: [], heap_arr2: [], n: int, m: int):
    heap_arr1.extend(heap_arr2)
    extend = (n + m) // 2
    for i in reversed(range(extend)):
        heapify_max_heap(heap_arr1, (n + m), i)

    return heap_arr1


def heapify_max_heap(heap_arr: [], n: int, index: int):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    if left_index < n and heap_arr[largest] < heap_arr[left_index]:
        largest = left_index

    if right_index < n and heap_arr[largest] < heap_arr[right_index]:
        largest = right_index

    if largest != index:
        heap_arr[largest], heap_arr[index] = heap_arr[index], heap_arr[largest]
        heapify_max_heap(heap_arr, n, largest)


if __name__ == '__main__':
    print(merge_two_binary_heaps([10, 5, 6, 2], [12, 7, 9, 1], 4, 4))
