def min_heap_max_heap(input_arr: [], n: int):
    extend = n // 2
    for i in reversed(range(extend)):
        heapify_max_heap(input_arr, n, i)

    return input_arr


def heapify_max_heap(input_arr: [], n: int, index: int):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < n and input_arr[largest] < input_arr[left_index]:
        largest = left_index

    if right_index < n and input_arr[largest] < input_arr[right_index]:
        largest = right_index

    if largest != index:
        input_arr[largest], input_arr[index] = input_arr[index], input_arr[largest]
        heapify_max_heap(input_arr, n, largest)


if __name__ == '__main__':
    print(min_heap_max_heap([1, 2, 3, 6, 7, 8], 6))
    print(min_heap_max_heap([3, 5, 6, 7, 9, 12, 7], 7))
