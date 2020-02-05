def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def leftRotate(arr, d, n):
    d = d % n
    gc = gcd(d,n)

    for i in range(gc):

        temp = arr[i]
        j = i
        while 1:
            k = j+d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp

def print(arr):
    for i in arr:
        print(i)

arr = [1,2,3,4,5,6,7,8,9,10,11,12]
leftRotate(arr,3,len(arr))
print(arr)