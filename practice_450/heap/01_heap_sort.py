def heap_build(input_arr: []):
    n = len(input_arr)
    for i in reversed(range(n)):
        heapify_min_arr(input_arr, n, i)


def heapify_min_arr(input_arr: [], n: int, index: int):
    smallest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < n and input_arr[left_index] < input_arr[smallest]:
        smallest = left_index

    if right_index < n and input_arr[right_index] < input_arr[smallest]:
        smallest = right_index

    if smallest != index:
        input_arr[smallest], input_arr[index] = input_arr[index], input_arr[smallest]
        heapify_min_arr(input_arr, n, smallest)


def delete_from_min_heap(heap_arr: []):
    n = len(heap_arr)
    heap_arr[0] = heap_arr[n - 1]
    i = 0
    n = n - 1
    while i < n:
        smallest = i
        left_index = 2 * smallest + 1
        right_index = 2 * smallest + 2
        left_value = heap_arr[left_index] if left_index < n else float('inf')
        right_value = heap_arr[right_index] if right_index < n else float('inf')
        smallest_comp = left_index if left_value < right_value else right_index
        if smallest_comp < n and heap_arr[i] > heap_arr[smallest_comp]:
            heap_arr[i], heap_arr[smallest_comp] = heap_arr[smallest_comp], heap_arr[i]
            i = smallest_comp
        else:
            break

    return heap_arr[:n]


def heap_sort(input_arr: []):
    heap_build(input_arr)
    n = len(input_arr)
    final_arr = []
    for i in range(n):
        element = input_arr[0]
        final_arr.append(element)
        input_arr = delete_from_min_heap(input_arr)

    return final_arr


if __name__ == '__main__':
    print(heap_sort([3, 1, 1, 6, 5, 7, 8, 9, 5]))
    print(heap_sort([10, 7, 8, 11]))
