def max_product_sub_array(arr: [], n):
    max_value = 1
    min_value = 1
    res = 1

    start_index = 0
    modify_initial_state = False

    for i in range(start_index, n):
        element = arr[i]
        if element > 0:
            modify_initial_state = True
            max_value = max(max_value, max_value * element)
            min_value = min(min_value, min_value * element)
        if element == 0:
            max_value = 1
            min_value = 1
        if element < 0:
            min_value, max_value = max_value, min_value
            min_value = min(min_value, min_value * element)
            curr_value = max_value * element
            if curr_value >= max_value:
                modify_initial_state = True
                max_value = curr_value
        res = max(max_value, res)
    if res == 1:
        if modify_initial_state:
            return 1
        else:
            if check_contains_zero(arr, n):
                return 0
            else:
                return min(arr)
    else:
        return res


def check_contains_zero(arr: [], n):
    for i in range(0, n):
        if arr[i] == 0:
            return True

    return False


def check_first_non_zero_index(arr: [], n, index):
    if index >= n:
        return n
    if arr[index] <= 0:
        return check_first_non_zero_index(arr, n, index + 1)
    else:
        return index


if __name__ == '__main__':
    # print(check_first_non_zero_index([0, 0, 1, 3, 0, 4], 6, 0))
    # print(check_first_non_zero_index([0, 0, -5, 0, 0], 5, 0))
    print(max_product_sub_array([6, -3, -10, 0, -2], 5))
    print(max_product_sub_array([0, 0, -5, 0, 0], 5))
    print(max_product_sub_array([-4], 1))
    print(max_product_sub_array([-1, -1], 2))
    print(max_product_sub_array([3, -7, -9, 2, -7, 5, -4, -8], 8))
