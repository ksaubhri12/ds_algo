import math


def aggressive_cows(arr: [], n, c):
    arr = sorted(arr)
    end = int(math.pow(10, 9))
    start = 0
    answer = None
    while start <= end:
        middle = start + (end - start) // 2
        cow = 1
        prev = arr[0]
        for i in range(1, n):
            element = arr[i]
            if element - prev >= middle:
                prev = element
                cow = cow + 1

            if cow == c:
                break

        if cow == c:
            answer = middle
            start = middle + 1
        else:
            end = middle - 1

    return answer


if __name__ == '__main__':
    print(aggressive_cows([1, 5, 8, 11, 13, 16], 6, 4))
