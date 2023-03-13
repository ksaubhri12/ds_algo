def find_missing_and_repeating(arr, n):
    b = None
    for i in range(0, n):
        element = abs(arr[i])
        index_to_go = element - 1
        if arr[index_to_go] > 0:
            arr[index_to_go] = -1 * arr[index_to_go]
        else:
            b = element
    a = None
    for i in range(0, n):
        if arr[i] > 0:
            a = i + 1
    return [b, a]


if __name__ == '__main__':
    print(find_missing_and_repeating([1, 3, 3], 3))
    print(find_missing_and_repeating([2, 2], 2))
    print(find_missing_and_repeating(
        [13, 33, 43, 16, 25, 19, 23, 31, 29, 35, 10, 2, 32, 11, 47, 15, 34, 46, 30, 26, 41, 18, 5, 17, 37, 39, 6, 4, 20,
         27, 9, 3, 8, 40, 24, 44, 14, 36, 7, 38, 12, 1, 42, 12, 28, 22, 45], 47))
