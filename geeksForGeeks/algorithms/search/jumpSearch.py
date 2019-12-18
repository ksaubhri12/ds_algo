import math
from geeksForGeeks.algorithms.search import linearSearch


def jumpSearch(arr, x):
    startIndex = 0
    jumpSize = int(math.sqrt(len(arr)))
    while startIndex < len(arr):
        if arr[startIndex] <= x <= arr[startIndex + jumpSize]:
            return startIndex+linearSearch.linearSearch(arr[startIndex:startIndex + jumpSize + 1], x)
        else:
            startIndex = jumpSize+startIndex+1
    return -1


print(jumpSearch([2, 3, 4, 10, 40, 100, 150, 200, 210, 320, 288, 400 ],210))
