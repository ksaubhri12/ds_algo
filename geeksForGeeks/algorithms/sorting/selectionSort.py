def selectionSort(arr):
    n = len(arr)
    i = 0

    while i < n - 1:
        min_index = i
        j = i + 1
        while j < n:
            if arr[j] < arr[min_index]:
                min_index = j
            j += 1
        temp = arr[min_index]
        arr[min_index] = arr[i]
        arr[i] = temp
        i += 1
    print(arr)


selectionSort([289, 18, 17, 90, 36, 188, 361, 3, 1, 0, 37])
selectionSort(["paper", "true", "soap", "floppy", "flower"])
