def get_negative_element_index(arr: [], start: int, end: int):
    if start > end:
        return -1

    if arr[start] < 0:
        return start

    middle_index = start + (end - start) // 2

    if middle_index > 1 and arr[middle_index - 1] >= 0 and arr[middle_index] < 0:
        return middle_index
    if arr[middle_index] >= 0:
        return get_negative_element_index(arr, middle_index + 1, end)
    else:
        return get_negative_element_index(arr, start, middle_index)


def get_count_negative_number(mat: [[]], max_row: int, max_col: int):
    input_arr = [mat[i][0] for i in range(max_col + 1)]
    index_in_first_col = get_negative_element_index(input_arr, 0, max_col)
    if index_in_first_col == -1:
        last_row = mat[max_row]
        index = get_negative_element_index(last_row, 0, max_col)
        if index == -1:
            return 0
        else:
            return max_col - index + 1

    else:
        curr_row = mat[index_in_first_col]
        total_rows = max_row - index_in_first_col
        total_element = total_rows * (max_col + 1)
        index = get_negative_element_index(curr_row, 0, max_col)
        partial = max_col - index + 1
        return partial + total_element


if __name__ == '__main__':
    input_mat = [
        [4, 3, 2, -1],
        [3, 2, 1, -1],
        [1, 1, -1, -2],
        [-1, -1, -2, -3]
    ]
    print(get_count_negative_number(input_mat, 3, 3))
