def binarySearch(arr, l, r, x):
    if r >= l:
        mid_index = int((r + l) / 2)
        if arr[mid_index] == x:
            return mid_index

        if arr[mid_index] > x:
            return binarySearch(arr, l, mid_index - 1, x)

        if arr[mid_index] < x:
            return binarySearch(arr, mid_index + 1, r, x)
    else:
        return -1


print(binarySearch([2, 3, 4, 10, 40], 0, 5, 10))
