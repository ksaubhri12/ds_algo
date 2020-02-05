def pushZeroToEndWithModification(arr):
    n = len(arr)
    if n == 1:
        return arr
    for i in range(n-1):
        if arr[i] != 0 and arr[i] == arr[i+1]:
            arr[i] = 2*arr[i+1]
            arr[i+1] = 0

    count = 0
    for i in range(n):
        if arr[i] != 0:
            arr[count],arr[i] = arr[i],arr[count]
            count = count + 1
    return arr

arr = [0, 2, 2, 2, 0, 6, 6, 0, 0, 8]
print(pushZeroToEndWithModification(arr))

