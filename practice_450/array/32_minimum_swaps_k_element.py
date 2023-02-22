def min_swaps(arr: [], n, k):
    count = 0
    for i in range(0, n):
        if arr[i] <= k:
            count = count + 1

    bad_count = 0
    for i in range(0, count):
        element = arr[i]
        if element > k:
            bad_count = bad_count + 1
    ans = bad_count
    for i in range(1, n):
        start = i
        end = start + count - 1
        if end >= n:
            break

        if arr[end] > k:
            bad_count = bad_count + 1

        if arr[start - 1] > k:
            bad_count = bad_count - 1
        ans = min(ans, bad_count)

    return ans


if __name__ == '__main__':
    print(min_swaps([2, 7, 9, 5, 8, 7, 4], 7, 6))
    print(min_swaps([2, 1, 5, 6, 3], 5, 3))
