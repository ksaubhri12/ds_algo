def unSortedSubArray(arr):
    startIndex = 0
    i = 0
    n = len(arr)
    endIndex = n - 1
    while i < n:
        if arr[i] > arr[i + 1]:
            startIndex = i
            break
        i += 1
    i = n - 1
    while i > 0:
        if arr[i] < arr[i - 1]:
            endIndex = i
            break
        i = i - 1
    minValue = min(arr[startIndex:endIndex + 1])
    maxValue = max(arr[startIndex:endIndex + 1])
    finalMinIndex = startIndex
    finalMaxIndex = endIndex

    for index in range(len(arr[:startIndex])):
        if arr[index] > minValue:
            minValue = arr[index]
            finalMinIndex = index
    for index in range(len(arr[endIndex + 1:])):
        if arr[index] < maxValue:
            maxValue = arr[index]
            finalMaxIndex = endIndex + index + 1
    return finalMinIndex, finalMaxIndex


print(unSortedSubArray([10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]))
print(unSortedSubArray([0, 1, 15, 25, 6, 7, 30, 40, 50]))
