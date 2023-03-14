def zero_sum_sub_arr(arr: [], n: int):
    prefix_sum = {}
    sum_value = 0
    prefix_sum[0] = 1
    for i in range(0, n):
        element = arr[i]
        sum_value = sum_value + element
        # if element == 0:
        #     set_key_in_dict(prefix_sum, 0)
        if sum_value in prefix_sum:
            prefix_sum[sum_value] = prefix_sum[sum_value] + 1
        else:
            prefix_sum[sum_value] = 1

    count = 0
    for value in prefix_sum.values():
        if value > 1:
            total_possible_arr = (value - 1) * value // 2
            count = count + total_possible_arr

    return count


def set_key_in_dict(dict_map: {}, key: int):
    if key in dict_map:
        dict_map[key] = dict_map[key] + 1
    else:
        dict_map[key] = 1


if __name__ == '__main__':
    print(zero_sum_sub_arr([6, -1, -3, 4, -2, 2, 4, 6, -12, -7], 10))
    print(zero_sum_sub_arr([0, 0, 5, 5, 0, 0], 6))
