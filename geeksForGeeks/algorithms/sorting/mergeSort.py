def mergeSort(arr):
    if len(arr) > 1:
        middle = int(len(arr) / 2)
        leftArray = mergeSort(arr[:middle])
        rightArray = mergeSort(arr[middle:])
        finalArray = merge(leftArray, rightArray)
        return finalArray
    return arr


def merge(leftArray, rightArray):
    leftArrayIndex = 0
    rightArrayIndex = 0
    finalArray = [None] * (len(leftArray) + len(rightArray))
    finalArrayIndex = 0

    while leftArrayIndex < len(leftArray) and rightArrayIndex < len(rightArray) and finalArrayIndex < len(
            leftArray) + len(rightArray):
        if leftArray[leftArrayIndex] <= rightArray[rightArrayIndex]:
            finalArray[finalArrayIndex] = leftArray[leftArrayIndex]
            leftArrayIndex += 1
        else:
            finalArray[finalArrayIndex] = rightArray[rightArrayIndex]
            rightArrayIndex += 1
        finalArrayIndex += 1
    if finalArrayIndex == len(leftArray) + len(rightArray):
        return finalArray
    if leftArrayIndex == len(leftArray):
        for value in rightArray[rightArrayIndex:]:
            finalArray[finalArrayIndex] = value
            finalArrayIndex += 1
        return finalArray
    if rightArrayIndex == len(rightArray):
        for value in leftArray[leftArrayIndex:]:
            finalArray[finalArrayIndex] = value
            finalArrayIndex += 1
        return finalArray


print(merge([11, 13, 15, 23, 27, 28, 30, 88], [6, 8, 88, 99, 100]))
print(mergeSort([289, 18, 17, 90, 36, 188, 361, 3, 1, 0, 37, 36]))
print(mergeSort([12, 11, 13, 5, 6, 7]))
