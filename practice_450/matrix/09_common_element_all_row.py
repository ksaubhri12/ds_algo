def common_element(matrix: [[]]):
    row_len = len(matrix)
    for i in range(0, row_len):
        matrix[i] = sorted(matrix[i])

    first_row = matrix[0]
    final_arr = []
    for i in range(0, len(first_row)):
        element_to_find = first_row[i]
        answer = True
        for j in range(1, row_len):
            complete_row = matrix[j]
            element_index = binary_search(complete_row, 0, len(complete_row) - 1, element_to_find)
            if element_index == -1:
                answer = False
        if answer:
            final_arr.append(element_to_find)

    return final_arr


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
    input_matrix = [
        [1, 2, 1, 4, 8],
        [3, 7, 8, 5, 1],
        [8, 7, 7, 3, 1],
        [8, 1, 2, 7, 9]
    ]
    print(common_element(input_matrix))
