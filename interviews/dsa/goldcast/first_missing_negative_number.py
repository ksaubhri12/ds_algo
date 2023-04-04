def get_negative_driver(arr: []):
    start = 0
    end = len(arr) - 1
    lowest = arr[start]
    highest = arr[end]
    return get_negative_number(arr, start, end, lowest, highest)


def get_negative_number(arr: [], start, end, lowest, highest):
    if start > end:
        return arr[start]

    if arr[0] >= 0:
        return -1

    middle_index = start + (end - start) // 2

    middle_element = arr[middle_index]
    if middle_element >= 0:
        return get_negative_number(arr, start, middle_index - 1, lowest, highest)
    elif middle_element < 0 and middle_element + 1 != arr[middle_index + 1]:
        return middle_element + 1
    else:
        value_check = get_negative_number(arr, start, middle_index, arr[start], arr[middle_index])
        if value_check == lowest:
            return value_check - 1
        elif lowest < value_check < highest:
            return value_check
        else:
            return get_negative_number(arr, middle_index + 1, end, arr[middle_index + 1], arr[end])


if __name__ == '__main__':
    input_arr = [-5, -3, -2, -1, 0, 1, 3, 4, 5]
    print(get_negative_driver(input_arr))
    # output = -4
    #
    input_arr = [0, 1, 3, 4, 5]
    print(get_negative_driver(input_arr))
    # output = -1
    #
    input_arr = [-5, -4, -3, -1, -1, 0, 1, 3, 4, 5]
    print(get_negative_driver(input_arr))
    # output = -6
    #
    input_arr = [-10, 1, 1, 2, 3]
    print(get_negative_driver(input_arr))
    #
    # [-5, -4, -4, -2, 0, 1, 3, 4, 5]
    #
    # [-10, -8, -9, -4, -3, -2]
