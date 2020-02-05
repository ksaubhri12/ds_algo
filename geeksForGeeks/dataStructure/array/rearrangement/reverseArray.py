def reverseArray(arrr):
    start = 0
    n = len(arrr)
    end = n - 1

    while start < end:
        arrr[start], arrr[end] = arrr[end], arrr[start]
        start += 1
        end = end - 1

    print(arrr)


arr = [1, 2, 4, 5, 8]
reverseArray(arr)
