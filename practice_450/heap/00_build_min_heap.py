def build_min_heap(input_arr: []):
    n = len(input_arr)
    for i in reversed(range(n)):
        heapify_min_arr(input_arr, n, i)

    return input_arr


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


if __name__ == '__main__':
    print(build_min_heap([9, 3, 2, 6, 7]))
