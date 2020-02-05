def moveAllZeroes(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count = count + 1
    while count < n:
        arr[count] = 0
        count += 1

    return arr

def moveZeroToEnd(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        if arr[i] != 0:
            arr[count], arr[i] = arr[i],arr[count]
            count += 1
    return arr

arr = [1,9,8,4,0,0,2,7,0,6,0]
# print(moveAllZeroes(arr))
print(moveZeroToEnd(arr))
