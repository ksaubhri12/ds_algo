def twoLargest(arr):
    largest = 0
    secondLargest = 0
    thirdLargest = 0
    for i in range(len(arr)):
        if arr[i] > largest:
            secondLargest , thirdLargest = largest,secondLargest
            largest = arr[i]
        if secondLargest < arr[i] < largest:
            thirdLargest = secondLargest
            secondLargest = arr[i]
        if thirdLargest < arr[i] < secondLargest:
            thirdLargest = arr[i]
    return largest,secondLargest,thirdLargest

arr = [12, 45, 1, -1, 45, 54, 23, 5, 0, -10]

print(twoLargest(arr))