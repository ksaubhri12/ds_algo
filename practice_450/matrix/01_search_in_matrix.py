def search_in_col_list(input_list, start_index, end_index, target):
    if target < input_list[start_index]:
        return None
    if input_list[end_index] < target:
        return None

    if input_list[start_index] == target:
        return start_index

    if input_list[end_index] == target:
        return end_index

    if input_list[start_index] < target < input_list[end_index]:
        return start_index

    middle_element_index = ((start_index + end_index) // 2)
    middle_element = input_list[middle_element_index]

    if target < middle_element:
        return search_in_col_list(input_list, start_index, middle_element_index, target)

    else:
        return search_in_col_list(input_list, middle_element_index, end_index, target)


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


def search_in_2d(matrix: [[int]], target: int):
    result_arr = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            result_arr.append(matrix[i][j])

    return binary_search(result_arr, 0, len(result_arr)-1, target) != -1




if __name__ == '__main__':
    print(search_in_2d([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
    print(search_in_2d([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
    print(search_in_2d([[1,3]],3))
