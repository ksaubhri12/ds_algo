def chocolate_distribution(arr: [], n, m):
    arr = sorted(arr)
    min_diff = float('inf')
    for i in range(0, n):
        end_index = i + m - 1
        if end_index < n:
            min_element = arr[i]
            max_element = arr[end_index]
            diff = max_element - min_element
            min_diff = min(min_diff, diff)

    return min_diff


if __name__ == '__main__':
    print(chocolate_distribution([3, 4, 1, 9, 56, 7, 9, 12], 8, 5))
    print(chocolate_distribution([7, 3, 2, 4, 9, 12, 56], 7, 3))
