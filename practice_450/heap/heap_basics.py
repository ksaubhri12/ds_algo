def insertion_in_max_heap(heap_arr: [], n: int, insert_element):
    n = n + 1
    heap_arr.append(insert_element)
    i = n - 1
    while i > 0:
        node = heap_arr[i]
        parent_node_index = (i - 1) // 2
        parent_node = heap_arr[parent_node_index]
        if parent_node >= node:
            break

        else:
            heap_arr[i], heap_arr[parent_node_index] = heap_arr[parent_node_index], heap_arr[i]
            i = parent_node_index

    return heap_arr


def deletion_from_heap_max(heap_arr: [], n):
    heap_arr[0] = heap_arr[n - 1]
    n = n - 1
    i = 0
    while i < n - 1:
        left = 2 * i + 1
        right = 2 * i + 2
        left_value = heap_arr[left] if left < n - 1 else float('-inf')
        right_value = heap_arr[right] if right < n - 1 else float('-inf')
        larger = left if left_value > right_value else right
        if larger < n - 1 and heap_arr[i] < heap_arr[larger]:
            heap_arr[i], heap_arr[larger] = heap_arr[larger], heap_arr[i]
            i = larger
        else:
            break

    return heap_arr[:n]


def heapify_arr(input_arr: [], n: int, index: int):
    largest = index
    left_child_index = 2 * index + 1
    right_child_index = 2 * index + 2
    if left_child_index < n and input_arr[left_child_index] > input_arr[largest]:
        largest = left_child_index

    if right_child_index < n and input_arr[right_child_index] > input_arr[largest]:
        largest = right_child_index

    if largest != index:
        input_arr[largest], input_arr[index] = input_arr[index], input_arr[largest]
        heapify_arr(input_arr, n, largest)


def build_max_heap(input_arr: []):
    n = len(input_arr)
    for i in reversed(range(0, n)):
        heapify_arr(input_arr, n, i)

    return input_arr


def heap_sort_arr(input_arr: []):
    build_max_heap(input_arr)
    final_arr = []
    n = len(input_arr)

    for i in range(n):
        size = n - i
        first_element = input_arr[0]
        final_arr.append(first_element)
        deletion_from_heap_max(input_arr, size)
    return list(reversed(final_arr))


if __name__ == '__main__':
    arr = [20, 10, 30, 5, 50, 40]
    print(heap_sort_arr(arr))

    input_data_arr = [50, 40, 45, 30, 20, 35, 10]
    print(insertion_in_max_heap(input_data_arr, 7, 60))
    print(insertion_in_max_heap(input_data_arr, 8, 28))
    print(insertion_in_max_heap(input_data_arr, 9, 41))
    print(deletion_from_heap_max(input_data_arr, 10))
