from geeksForGeeks.algorithms.search import binarySearch


def exponentialSearch(arr, x):
    n = len(arr)
    if arr[0] == x:
        return 0
    i = 1
    while i < n and arr[i] <= x:
        i = i * 2
    return binarySearch.binarySearch(arr, i / 2, min(i, n), x)


print(exponentialSearch([2, 3, 4, 10, 40],3))
