def rearrangeArrayEvenOddRule(arr):
    sortedArray = sorted(arr)
    n = len(arr)
    low = 0
    high = len(arr)
    finalArray = [None]*len(arr)
    curr = n -1
    while curr >= 0:
        if n%2 == 0:
            finalArray[curr] = sortedArray[high-1]
            curr = curr -1
            finalArray[curr] = sortedArray[low]
            curr = curr -1
            high = high - 1
            low = low + 1
        else:
            finalArray[curr] = sortedArray[low]
            curr = curr -1
            if curr < 0:
                break
            finalArray[curr] = sortedArray[high-1]
            curr = curr -1
            high = high -1
            low = low + 1
    return  finalArray

arr = [1, 2, 3, 4, 5, 6, 7]

print(rearrangeArrayEvenOddRule(arr))
