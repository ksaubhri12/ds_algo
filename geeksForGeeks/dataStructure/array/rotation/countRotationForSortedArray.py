def countRotation(arr, low, high):
    if high < low:
        return 0
    if high == low:
        return low

    mid = low + (high - low) / 2
    mid = int(mid)

    if arr[mid] > arr[mid + 1]:
        return mid + 1

    if arr[mid] < arr[mid - 1]:
        return mid

    if arr[high] > arr[mid]:
        return countRotation(arr, low, mid - 1)

    return countRotation(arr, mid + 1, high)


arr = [7, 9, 11, 12, 15]
n = len(arr)
print(countRotation(arr, 0, n - 1))
