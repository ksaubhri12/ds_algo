def smallest_subset_sum_greater_all_element(arr: [], n):
    arr = sorted(arr, reverse=True)
    total_sum = sum(arr)
    curr_sum = 0

    for i in range(0, n):
        if curr_sum > total_sum:
            return i

        curr_sum = curr_sum + arr[i]
        total_sum = total_sum - arr[i]

    return 1


if __name__ == '__main__':
    print(smallest_subset_sum_greater_all_element([2, 17, 7, 3], 4))
    print(smallest_subset_sum_greater_all_element([20, 12, 18, 4], 4))
