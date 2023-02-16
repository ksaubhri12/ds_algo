def smallest_sub_array_given_value(arr: [], n, k):
    if arr[0] == k:
        return 1
    start = 0
    end = start + 1
    sum_value = arr[start] + arr[end]
    while end < n:
        if sum_value >= k:
            return max(1, end - start)
        elif sum_value > k:

            element_to_remove = arr[start]
            start = start + 1

            sum_value = sum_value - element_to_remove

        elif sum_value < k:

            next_element_to_add = arr[end + 1]
            end = end + 1
            sum_value = sum_value + next_element_to_add

    return 0


if __name__ == '__main__':
    print(smallest_sub_array_given_value([2, 3, 1, 2, 4, 3], 6, 7))
    print(smallest_sub_array_given_value([1, 1, 1, 1, 1, 1, 1, 1], 8, 11))
    print(smallest_sub_array_given_value([1, 4, 4], 3, 4))
    print(smallest_sub_array_given_value([1, 2, 3, 4, 5], 5, 11))
