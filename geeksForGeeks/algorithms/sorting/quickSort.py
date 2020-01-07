def quickSort(arr, startIndex, endIndex):
    if endIndex > startIndex:
        pIndex = partition(arr, startIndex, endIndex)
        quickSort(arr, startIndex, pIndex - 1)
        quickSort(arr, pIndex + 1, endIndex)


def partition(arr, startIndex, endIndex):
    pivot = arr[endIndex]
    partitionIndex = startIndex
    i = startIndex
    while i < endIndex - 1:
        if arr[i] <= pivot:
            arr[i], arr[partitionIndex] = arr[partitionIndex], arr[i]
            partitionIndex += 1
        i = i + 1
    arr[partitionIndex], arr[endIndex] = arr[endIndex], arr[partitionIndex]

    return partitionIndex


arr = [10, 80, 30, 90, 40, 50, 70]
quickSort(arr, 0, len(arr) - 1)
print(arr)
