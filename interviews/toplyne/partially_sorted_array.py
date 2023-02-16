def partially_sorted_arr(arr: [], n):
    result_arr = []
    pre_compute_formula_arr = []
    curr_index = -1
    changing_value_arr = []
    for i in range(0, n):
        element = arr[i]
        actual_value = get_base_4_lsb(element)
        if curr_index == -1:
            pre_compute_formula_arr.append(actual_value)
            curr_index = 0
            changing_value_arr.append(i)

        last_value_in_pre_compute = pre_compute_formula_arr[curr_index]
        if last_value_in_pre_compute != actual_value:
            pre_compute_formula_arr.append(actual_value)
            changing_value_arr.append(i)
            curr_index = curr_index + 1

    changes_len = len(changing_value_arr)
    start = 0
    end = start + 1
    while end < changes_len:
        value_range = get_range_with_index(start)
        start_value = value_range[0]
        end_value = value_range[1]

        value_dict = {}
        for i in range(start_value, end_value):
            count = get_count_of_element_in_sub_arr(arr, changing_value_arr[start], changing_value_arr[end] - 1, i)
            value_dict[i] = count

        for key in value_dict.keys():
            count = value_dict[key]
            for i in range(0, count):
                result_arr.append(key)

        start = start + 1
        end = start + 1

    return result_arr


def get_count_of_element_in_sub_arr(arr: [], start, end, num):
    count = 0
    for i in range(start, end + 1):
        element = arr[i]
        if element == num:
            count = count + 1
    return count


def get_range_with_index(index):
    first_element = index * 16
    last_element = first_element + 15
    return [first_element, last_element]


def get_base_4_lsb(arr):
    return (arr // 16) * 16


def get_dict_from_arr(arr: [], start, end):
    value_dict = {}
    for i in range(start, end + 1):
        if i in value_dict:
            value_dict[i] = value_dict[i] + 1
        else:
            value_dict[i] = 1

    return value_dict


if __name__ == '__main__':
    print(partially_sorted_arr([2, 2, 4, 3, 6, 5, 9, 17, 18, 20, 19, 36, 34, 35], 14))
