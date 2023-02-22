def duplicate_in_array(arr: [], n):
    arr = sorted(arr)
    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            return arr[i]


if __name__ == '__main__':
    print(duplicate_in_array([3, 3, 3, 3], 4))
    print(duplicate_in_array([1, 2, 3, 4, 2], 5))
