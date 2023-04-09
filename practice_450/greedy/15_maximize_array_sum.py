def maximize_arr_sum(arr: [], n, k):
    arr = sorted(arr)
    count = 0
    for i in range(0, n):
        if count == k:
            break
        if arr[i] < 0:
            count = count + 1
            arr[i] = arr[i] * -1

    if count == k:
        return sum(arr)

    arr = sorted(arr)

    left_count = k - count
    if left_count % 2 != 0:
        arr[0] = arr[0] * -1

    return sum(arr)


if __name__ == '__main__':
    print(maximize_arr_sum([1, 2, -3, 4, 5], 5, 1))
    print(maximize_arr_sum([5, -2, 5, -4, 5, -12, 5, 5, 5, 20], 10, 5))
    print(maximize_arr_sum([1, 2, 3, 4, 5, ], 5, 5))
    print(maximize_arr_sum([-1, -2, -3, -4, -5], 5, 10))
