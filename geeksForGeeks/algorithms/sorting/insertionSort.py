def insertionSort(arr):
    n = len(arr)
    i = 1
    while i < n:
        value = arr[i]
        hole = i
        while hole > 0 and arr[hole - 1] > value:
            arr[hole] = arr[hole - 1]
            hole = hole - 1
        arr[hole] = value
        i = i + 1
    print(arr)


insertionSort([289, 18, 17, 90, 36, 188, 361, 3, 1, 0, 37])
