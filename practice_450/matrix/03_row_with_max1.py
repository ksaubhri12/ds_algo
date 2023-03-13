def row_with_max_1(matrix: [[]]):
    min_1_index_row = -1
    min_1_index = len(matrix[0]) + 1
    for i in range(0, len(matrix)):
        input_list = matrix[i]
        index = binary_search(input_list, 0, len(input_list) - 1, 1)
        if -1 < index < min_1_index:
            min_1_index = index
            min_1_index_row = i

    return min_1_index_row


def binary_search(arr: [], start: int, end: int, k):
    if start >= end and arr[start] == k:
        return start

    if start >= end and arr[start] != k:
        return -1

    middle_index = int((start + end) / 2)

    middle_element = arr[middle_index]

    if middle_element < k:
        return binary_search(arr, middle_index + 1, end, k)
    else:
        return binary_search(arr, start, middle_index, k)


if __name__ == '__main__':
    print(sorted([3, 23, 4]))

    input_matrix = [[0, 1, 1, 1],
                    [0, 0, 1, 1],
                    [1, 1, 1, 1],
                    [0, 0, 0, 0]]

    print(row_with_max_1(input_matrix))

    input_matrix = [[0, 0, ], [0, 0]]
    print(row_with_max_1(input_matrix))
