import math


def maximize_arr_sum(arr: [], n):
    arr = sorted(arr)
    result = 0
    for i in range(0, n):
        curr_val = arr[i] * i
        result = result + curr_val

    sign = 1
    if result < 0:
        sign = -1

    return sign * int(abs(result) % (math.pow(10, 9) + 7))


if __name__ == '__main__':
    print(maximize_arr_sum([5, 3, 2, 4, 1], 5))
    print(maximize_arr_sum([1, 2, 3], 3))
