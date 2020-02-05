def minSwaps(arr,k):
    n = len(arr)
    count = 0
    for i in range(n):
        if arr[i] <= k:
            count += 1
    bad = 0
    for i in range(count):
        if arr[i] > k:
            bad += 1
    j = count
    for i in range(0,n):
        if j == n:
            break
        ans = 0
        for y in range(i,j):
            if arr[y] > k:
                ans += 1
        bad = min(ans, bad)
        j = j+1
    return bad

arr = [2,1,5,6,3]
print(minSwaps(arr,3))
