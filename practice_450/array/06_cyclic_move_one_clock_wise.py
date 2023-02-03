def cyclic_move_one_clock_wise(arr: [], n):
    last_element = arr[n - 1]
    temp = arr[0]
    for i in range(1, n - 1):
        element_to_pick = arr[i]
        arr[i] = temp
        temp = element_to_pick

    arr[n-1] = temp
    arr[0] = last_element

    return arr


if __name__ == '__main__':
    print(cyclic_move_one_clock_wise([1, 2, 3, 4, 5], 5))

