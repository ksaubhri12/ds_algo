def max_sub_array_sum(arr: [], n):
    max_sum_index_arr = [arr[0]]

    for i in range(1, n):
        sum_at_index_i = max(max_sum_index_arr[i - 1] + arr[i], arr[i])
        max_sum_index_arr.append(sum_at_index_i)

    return max_sum_index_arr


def max_sub_array_sum_v2(arr: [], n):
    sum_at_index_i = arr[0]
    max_sum_so_far = arr[0]
    for i in range(1, n):
        sum_at_index_i = max(sum_at_index_i + arr[i], arr[i])
        max_sum_so_far = max(max_sum_so_far, sum_at_index_i)
        # print(sum_at_index_i)

    return max_sum_so_far


if __name__ == '__main__':
    print(max_sub_array_sum([1, 2, 3, -2, 5], 5))
    print(max_sub_array_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4], 9))
    print(max_sub_array_sum([-1, -2, 1, 2, 3, -8, -9], 7))
    print(max_sub_array_sum_v2([1, 2, 3, -2, 5], 5))
    print(max_sub_array_sum_v2([-2, 1, -3, 4, -1, 2, 1, -5, 4], 9))
    print(max_sub_array_sum_v2([-1, -2, 1, 2, 3, -8, -9], 7))
