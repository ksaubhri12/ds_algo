def product_array_puzzle(arr: [], n):
    is_zero_present = False
    zero_count = 0
    multiply_sum = 1
    for i in range(0, len(arr)):
        if arr[i] != 0:
            multiply_sum = multiply_sum * arr[i]
        else:
            is_zero_present = True
            zero_count = zero_count + 1

    final_arr = []
    if zero_count > 1:
        final_arr = [0]*n
        return final_arr

    for i in range(0, n):

        if is_zero_present and arr[i] != 0:
            value = 0
        elif arr[i] != 0:
            value = multiply_sum // arr[i]
        else:
            value = multiply_sum
        final_arr.append(value)

    return final_arr


if __name__ == '__main__':
    print(product_array_puzzle([10, 3, 5, 6, 2], 5))
    print(product_array_puzzle([12, 0], 2))
    arr = [258037519535308800, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 258037519535308800, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0 ]
    print(product_array_puzzle(arr, 28))
