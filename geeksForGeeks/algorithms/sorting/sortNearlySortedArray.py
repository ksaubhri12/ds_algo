def sortNearlySortedArray(arr, k):
    visited_index = []
    n = len(arr)
    i = 0
    while len(visited_index) < n:

        if i not in visited_index:
            visited_index.append(i)
            if arr[i + 1:i + k + 2]:
                minValue = min(arr[i + 1:i + k + 2])
                if minValue < arr[i]:
                    minValueIndex = arr.index(minValue)
                    arr[i], arr[minValueIndex] = arr[minValueIndex], arr[i]
                    visited_index.append(minValueIndex)
        i = i + 1
    return arr


arr = [6, 5, 3, 2, 8, 10, 9]
k = 3

print(sortNearlySortedArray(arr, k))

arr1 = [10, 9, 8, 7, 4, 70, 60, 50]
k = 4
print(sortNearlySortedArray(arr1, k))
