def min_max(arr: [], n: int):
    min_element = arr[0]
    max_element = arr[0]

    for i in range(0, n):
        min_element = min(min_element, arr[i])
        max_element = max(max_element, arr[i])

    return min_element, max_element


if __name__ == '__main__':
    print(min_max([7, 10, 11, 23, 17, 9, 8], 6))
