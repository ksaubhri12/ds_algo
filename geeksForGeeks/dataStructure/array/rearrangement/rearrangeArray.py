def rearrangeArray(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] != i and arr[i] != -1:
            x = arr[i]

            while arr[x] != x and arr[x] != -1:
                y = arr[x]
                arr[x] = x
                x = y
            arr[x] = x
            if arr[i] != i:
                arr[i] = -1
    return arr


arr = [-1, -1, 6, 1, 9, 3, 8, -1, 4, -1]
print(rearrangeArray(arr))
# arr1 = [19, 7, 0, 3, 18, 15, 12, 6, 1, 8, 11, 10, 9, 5, 13, 16, 2, 14, 17, 4]
# print(rearrangeArray(arr1))
