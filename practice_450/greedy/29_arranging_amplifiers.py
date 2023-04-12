def arranging_amplifiers(arr: [], n):
    arr = sorted(arr, reverse=True)
    one_count = 0
    for i in range(0, n):
        if arr[i] == 1:
            one_count = one_count + 1

    remaining_element_count = n - one_count
    if remaining_element_count == 2 and arr[0] == 3 and arr[1] == 2:
        c = 0
        for i in range(0, one_count):
            c = c + 1
            arr[i] = 1
        arr[c] = 2
        arr[c+1] = 3

        return arr

    if one_count != 0:
        arr = arr[0:remaining_element_count] + arr[remaining_element_count:]
    return arr


if __name__ == '__main__':
    print(arranging_amplifiers([4, 5, 6], 3))
    print(arranging_amplifiers([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3], 12))
