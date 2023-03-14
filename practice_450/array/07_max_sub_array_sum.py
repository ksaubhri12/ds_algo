# Lets build one array where we take the max sum for that index.
# If we start from first index sum will be equal to the value
# Now for next element either we can include it in with previous sum
# Or we can see if current element is itself greater than the sum with last array.

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
