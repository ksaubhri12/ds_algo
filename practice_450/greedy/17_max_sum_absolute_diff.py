def max_sum_absolute_diff(arr: [], n):
    sorted_arr = sorted(arr)
    reverse_sorted_arr = sorted(arr, reverse=True)
    i = 0
    j = 0
    while i < n:
        arr[i] = sorted_arr[j]
        if i + 1 < n:
            arr[i + 1] = reverse_sorted_arr[j]
        j = j + 1
        i = i + 2

    result = 0
    for i in range(0, n):
        if i == n - 1:
            j = 0
        else:
            j = i + 1

        diff = arr[i] - arr[j]
        result = result + abs(diff)

    return result


if __name__ == '__main__':
    print(max_sum_absolute_diff([3, 4, 2, 9, 1, 5], 6))
    print(max_sum_absolute_diff([1, 2, 3, 4, 5], 5))
    print(max_sum_absolute_diff([1, 2, 4, 8], 4))
    print(max_sum_absolute_diff([1, 2, 8, 3], 4))
