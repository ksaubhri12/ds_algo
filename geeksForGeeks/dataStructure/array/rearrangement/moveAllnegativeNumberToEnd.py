def moveAllNegativeNumberToEnd(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        if arr[i] >= 0:
            arr[count],arr[i] = arr[i],arr[count]
            count += 1
    return arr[:count]

arr = [1,-1,3,2,-7,-5,11,6]
print(moveAllNegativeNumberToEnd(arr))
