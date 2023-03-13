def first_and_last_occurrence(arr: [], n, k, ):
    return [first_occurrence(arr, 0, n - 1, k), last_occurrence(arr, 0, n - 1, k, n)]


def first_occurrence(arr: [], start: int, end: int, k):
    if start > end:
        return -1
    middle = start + (end - start) // 2
    if arr[middle] == k and (middle == 0 or k > arr[middle - 1]):
        return middle

    elif k > arr[middle]:
        return first_occurrence(arr, middle + 1, end, k)
    else:
        return first_occurrence(arr, start, middle - 1, k)


def last_occurrence(arr: [], start: int, end: int, k, n):
    if start > end:
        return -1

    middle = start + (end - start) // 2
    if arr[middle] == k and (middle == n - 1 or arr[middle + 1] > k):
        return middle
    elif k < arr[middle]:
        return last_occurrence(arr, start, middle - 1, k, n)
    else:
        return last_occurrence(arr, middle, end, k, n)


if __name__ == '__main__':
    print(first_and_last_occurrence([1, 1, 3, 5, 5, 5, 5, 67, 123, 125], 9, 5))
    print(first_and_last_occurrence([1, 3, 5, 5, 5, 5, 7, 123, 125], 9, 7))
    print(first_and_last_occurrence(
        [1, 1, 1, 2, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10], 30, 8))
