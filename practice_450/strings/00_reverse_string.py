def reverse_string(arr: []):
    n = len(arr)
    start = 0
    end = n - 1
    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        start = start + 1
        end = end - 1

    return arr


if __name__ == '__main__':
    print(reverse_string(["h", "e", "l", "l", "o"]))
    print(reverse_string(["H", "a", "n", "n", "a", "h"]))
