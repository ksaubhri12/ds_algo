def check(arr):
    INT_MIN = float("-infinity")
    INT_MAX = float("infinity")
    n = len(arr)
    flag = True
    for i in range(1, n):
        if arr[i - 1] < arr[i] < INT_MAX and arr[i] > INT_MIN:
            INT_MIN = arr[i-1]
        elif arr[i] < arr[i-1] and arr[i] < INT_MAX and arr [i] > INT_MIN:
            INT_MAX = arr[i-1]
        else:
            flag = False
            break
    if flag:
        print("Yes")
    else:
        print("No")

arr = [5123, 3300, 783, 1111, 890]
check(arr)

