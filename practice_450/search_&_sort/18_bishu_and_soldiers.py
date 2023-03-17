def bishu_soldiers(arr: [], m):
    arr = sorted(arr)
    n = len(arr)
    prefix_sum_arr = [None] * n
    prefix_sum_arr[0] = arr[0]
    for i in range(1, n):
        prefix_sum_arr[i] = prefix_sum_arr[i - 1] + arr[i]
    count = upper_bound(arr, 0, n - 1, m + 1)
    return count, prefix_sum_arr[count - 1]


# Finding element count lesser than the k
def upper_bound(arr: [], start: int, end: int, k):
    if start > end:
        return start
    middle = start + (end - start) // 2
    middle_element = arr[middle]

    if middle_element == k:
        return upper_bound(arr, start, middle - 1, k)

    if middle_element > k:
        return upper_bound(arr, start, middle - 1, k)

    else:
        return upper_bound(arr, middle + 1, end, k)


if __name__ == '__main__':
    print(bishu_soldiers([1, 2, 3, 4, 5, 6, 7], 3))
    print(bishu_soldiers([1, 2, 3, 4, 5, 6, 7], 10))
