def sub_array_sum_given_value(arr: [], n, k):
    start__index = 0
    curr_sum = arr[0]
    for i in range(1, n):
        curr_sum = curr_sum + arr[i]
        while curr_sum > k:
            curr_sum = curr_sum - arr[start__index]
            start__index = start__index + 1
        if curr_sum == k:
            return [i, start__index]

    return [-1, -1]


def smallest_sub_array_with_sum_greater_than_equal_value(arr: [], n, k):
    curr_sum = 0
    min_len = n + 1
    start = 0
    end = 0
    while end < n:
        while curr_sum < k and end < n:
            curr_sum = curr_sum + arr[end]
            end = end + 1

        while curr_sum >= k and start < n:
            if end - start < min_len:
                print(start, end, curr_sum)
                min_len = end - start

            curr_sum = curr_sum - arr[start]
            start = start + 1

    if min_len == n + 1:
        return 0
    else:
        return min_len


if __name__ == '__main__':
    # print(smallest_sub_array_with_sum_greater_than_equal_value([2, 3, 1, 2, 4, 3], 6, 7))
    # print(smallest_sub_array_with_sum_greater_than_equal_value([1, 1, 1, 1, 1, 1, 1, 1], 8, 11))
    print(smallest_sub_array_with_sum_greater_than_equal_value([1, 4, 4], 3, 4))
    # print(smallest_sub_array_given_value([1, 2, 3, 4, 5], 5, 11))
