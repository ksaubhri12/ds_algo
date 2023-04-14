import math


def max_product_sub_array(arr: [], n):
    if len(arr) == 1:
        return arr[0]
    positive_count = 0
    negative_count = 0
    zero_count = 0
    max_negative = float('-inf')
    prod = 1
    for i in range(0, n):
        if arr[i] > 0:
            positive_count = positive_count + 1
        elif arr[i] == 0:
            zero_count = zero_count + 1
        else:
            max_negative = max(max_negative, arr[i])
            negative_count = negative_count + 1
        if arr[i] != 0:
            prod = prod * arr[i]

    if zero_count == n:
        return 0
    elif negative_count == 1 and zero_count + negative_count == n:
        return 0
    elif negative_count % 2 != 0:
        prod = int(prod / max_negative)

    return int((int(prod) % (math.pow(10, 9) + 7)))


if __name__ == '__main__':
    arr_in = [7, -2, 7, -1, 2, -3, -10, -2, -9, 6, -5, -10, 9, 4, -5, 6, 0, 2, -10, -5, -6, 1, -6, 6, -3, 7, 7, -9, -10,
              -4, -9, 4, 9, 10, 3, -7, -6, 6, 3, 7, -3, -2, -10, -2, 10, -3, -9, 0, 7, -1, -3, 5, -5, -4, -3, 2, 3, 2,
              -7, -8, 9, 10, 10, 2, 4, 2, -8, 2, -3]
    print(max_product_sub_array(arr_in, 69))
    print(max_product_sub_array([-4, 0, 7, 10, -5, -3, -5, 5, 0], 9))
    print(max_product_sub_array([-1, -1, -2, 4, 3], 5))
