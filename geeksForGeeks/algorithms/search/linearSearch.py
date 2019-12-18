def linearSearch(arr , x):
    for index in range(len(arr)):
        if arr[index] == x:
            return index
    return -1



# x = linearSearch([1,2,4,5],4)
# print(x)