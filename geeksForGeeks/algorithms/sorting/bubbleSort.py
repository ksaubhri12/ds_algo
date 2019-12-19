def bubbleSort(arr):
    n = len(arr)
    i = 0
    while i < n - 1:
        swap = False
        j = 0
        while j < n - i - 1:
            if arr[j] < arr[j + 1]:
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp
                swap = True
            j += 1
        if not swap:
            break
        i += 1
    print(arr)


bubbleSort([5, 1, 4, 2, 8])
bubbleSort([289, 18, 17, 90, 36, 188, 361, 3, 1, 0, 37])
