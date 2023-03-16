def count_triplet(arr: [], n, k):
    arr = sorted(arr)
    count = 0
    for i in range(0, n):
        value = k - arr[i]
        count = count + upper_bound_v2(arr[i + 1:], value, len(arr[i + 1:]) - 1)
    return count


# Finding element count lesser than k using sliding window
def upper_bound_v2(arr: [], value, n):
    start = 0
    end = n - 1
    count = 0
    while start <= end:
        sum_value = arr[start] + arr[end]
        if sum_value >= value:
            end = end - 1
        else:
            start = start + 1
            count = count + 1

    return count


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
    print(count_triplet([30, 8, 23, 6, 10, 9, 31, 7, 19, 20, 1, 33, 21, 27, 28, 3, 25, 26], 18, 86))
    print(count_triplet([-2, 0, 1, 3], 4, 2))
    print(count_triplet([5, 1, 3, 4, 7], 5, 12))
